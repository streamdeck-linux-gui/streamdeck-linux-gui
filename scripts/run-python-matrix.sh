#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

DEFAULT_VERSIONS=("3.10" "3.11" "3.12" "3.14")
VERSIONS=("${DEFAULT_VERSIONS[@]}")
RUN_IN_PARALLEL=0
RUN_LINT=1
RUN_TESTS=1

usage() {
    cat <<'EOF'
Run local lint/test matrix for supported Python versions.

Usage:
  bash scripts/run-python-matrix.sh [options]

Options:
  --parallel                Run versions in parallel (isolated envs per version).
  --versions V1,V2,...      Override matrix versions (default: 3.10,3.11,3.12,3.14).
  --lint-only               Run lint only.
  --test-only               Run tests only.
  -h, --help                Show this help.
EOF
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --parallel)
            RUN_IN_PARALLEL=1
            shift
            ;;
        --versions)
            shift
            IFS=',' read -r -a VERSIONS <<< "${1:-}"
            shift
            ;;
        --lint-only)
            RUN_LINT=1
            RUN_TESTS=0
            shift
            ;;
        --test-only)
            RUN_LINT=0
            RUN_TESTS=1
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "Unknown option: $1" >&2
            usage
            exit 1
            ;;
    esac
done

if [[ ${#VERSIONS[@]} -eq 0 ]]; then
    echo "No Python versions provided." >&2
    exit 1
fi

if [[ "$RUN_LINT" -eq 0 && "$RUN_TESTS" -eq 0 ]]; then
    echo "Nothing to run: enable lint and/or tests." >&2
    exit 1
fi

poetry_version_for() {
    echo "2.3.2"
}

resolve_python_bin() {
    local python_version="$1"

    if command -v pyenv >/dev/null 2>&1; then
        local prefix=""
        if prefix="$(pyenv prefix "$python_version" 2>/dev/null)"; then
            if [[ -x "${prefix}/bin/python" ]]; then
                echo "${prefix}/bin/python"
                return 0
            fi
            if [[ -x "${prefix}/bin/python${python_version}" ]]; then
                echo "${prefix}/bin/python${python_version}"
                return 0
            fi
        fi
    fi

    if command -v "python${python_version}" >/dev/null 2>&1; then
        command -v "python${python_version}"
        return 0
    fi

    echo "Python ${python_version} not found (pyenv nor system PATH)." >&2
    return 1
}

run_case() {
    local python_version="$1"
    local python_bin=""
    local poetry_version=""
    local version_id="${python_version//./}"
    local case_root="${TMPDIR:-/tmp}/streamdeck-matrix/${version_id}"
    local tool_venv="${case_root}/tool-venv"
    local poetry_venvs="${case_root}/poetry-venvs"
    local poetry_config="${case_root}/poetry-config"
    local poetry_cache="${case_root}/poetry-cache"
    local pip_cache="${case_root}/pip-cache"
    local mypy_cache="${case_root}/mypy-cache"
    local pytest_temp="${case_root}/pytest-temp"

    python_bin="$(resolve_python_bin "$python_version")"
    poetry_version="$(poetry_version_for "$python_version")"

    rm -rf "$case_root"
    mkdir -p "$case_root"

    echo "[${python_version}] Python: ${python_bin}"
    echo "[${python_version}] Poetry: ${poetry_version}"

    "${python_bin}" -m venv "$tool_venv"
    # shellcheck disable=SC1090
    source "${tool_venv}/bin/activate"

    python -m pip install -q --upgrade pip
    python -m pip install -q "poetry==${poetry_version}"

    export POETRY_VIRTUALENVS_CREATE=true
    export POETRY_VIRTUALENVS_IN_PROJECT=false
    export POETRY_VIRTUALENVS_PATH="$poetry_venvs"
    export POETRY_CONFIG_DIR="$poetry_config"
    export POETRY_CACHE_DIR="$poetry_cache"
    export PIP_CACHE_DIR="$pip_cache"
    export MYPY_CACHE_DIR="$mypy_cache"

    cd "$REPO_ROOT"
    poetry env use "$python_bin" >/dev/null
    poetry install --no-interaction --no-root --no-ansi >/dev/null
    poetry install --no-interaction --no-ansi >/dev/null

    if [[ "$RUN_LINT" -eq 1 ]]; then
        ./scripts/lint.sh
    fi

    if [[ "$RUN_TESTS" -eq 1 ]]; then
        QT_QPA_PLATFORM=offscreen \
        PYTEST_ADDOPTS="--basetemp=${pytest_temp} -p no:cacheprovider" \
        poetry run pytest tests/ -q
    fi

    deactivate
    rm -rf "$tool_venv"
    echo "[${python_version}] PASS"
}

LOG_ROOT="${TMPDIR:-/tmp}/streamdeck-matrix-logs/$(date +%Y%m%d-%H%M%S)"
mkdir -p "$LOG_ROOT"

echo "Repository: ${REPO_ROOT}"
echo "Versions: ${VERSIONS[*]}"
echo "Mode: $([[ "$RUN_IN_PARALLEL" -eq 1 ]] && echo parallel || echo sequential)"
echo "Logs: ${LOG_ROOT}"

if [[ "$RUN_IN_PARALLEL" -eq 1 ]]; then
    declare -A PID_TO_VERSION=()
    pids=()

    for version in "${VERSIONS[@]}"; do
        (
            set -euo pipefail
            run_case "$version"
        ) >"${LOG_ROOT}/${version}.log" 2>&1 &

        pid=$!
        pids+=("$pid")
        PID_TO_VERSION["$pid"]="$version"
    done

    failures=0
    for pid in "${pids[@]}"; do
        if wait "$pid"; then
            echo "[PASS] ${PID_TO_VERSION[$pid]}"
        else
            echo "[FAIL] ${PID_TO_VERSION[$pid]} (see ${LOG_ROOT}/${PID_TO_VERSION[$pid]}.log)"
            failures=1
        fi
    done

    if [[ "$failures" -ne 0 ]]; then
        exit 1
    fi
else
    for version in "${VERSIONS[@]}"; do
        if run_case "$version" >"${LOG_ROOT}/${version}.log" 2>&1; then
            echo "[PASS] ${version}"
        else
            echo "[FAIL] ${version} (see ${LOG_ROOT}/${version}.log)"
            exit 1
        fi
    done
fi

echo "Matrix finished successfully."
echo "Detailed logs: ${LOG_ROOT}"
