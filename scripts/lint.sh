#!/bin/bash
set -euo pipefail

# if arg --fix is passed, fix the code
enable_fix=0
black_flag="--check --diff"
isort_flag="--check --diff"
if [[ $# -eq 1 ]] && [[ $1 == "--fix" ]]; then
    enable_fix=1
    black_flag=""
    isort_flag=""
fi

set -x

poetry run mypy --ignore-missing-imports streamdeck_ui/ --exclude 'ui_main.py|resources_rc.py|ui_settings.py|ui_button.py'
poetry run isort $isort_flag streamdeck_ui/ tests/ --skip ui_main.py --skip resources_rc.py --skip ui_settings.py  --skip ui_button.py --line-length 120
poetry run black $black_flag streamdeck_ui/ tests/ --exclude 'ui_main.py|resources_rc.py|ui_settings.py|ui_button.py' --line-length 120
poetry run flake8 streamdeck_ui/ tests/ --ignore F403,F401,W503 --exclude ui_main.py,resources_rc.py,ui_settings.py,ui_button.py

safety_args=(check --policy-file .safety-policy.yml)
python_minor="$(poetry run python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
if [[ "$python_minor" == "3.8" ]]; then
    # NOTE: safety v2.4.0b2 does not apply policy ignore-vulnerabilities while scanning installed envs.
    # Keep explicit ignores for unresolved Python 3.8-only CVEs until 3.8 support is dropped.
    safety_args+=(
        -i 77744
        -i 82331
        -i 84031
        -i 77745
        -i 82332
        -i 76752
        -i 82918
        -i 79883
        -i 83159
    )
fi
poetry run safety "${safety_args[@]}"
poetry run bandit -r streamdeck_ui/
