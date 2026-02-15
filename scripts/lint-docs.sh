#!/bin/bash
set -euo pipefail

if ! command -v npx >/dev/null 2>&1; then
    echo "Error: npx is required to lint Markdown files. Install Node.js and npm." >&2
    exit 1
fi

set -x
npx --yes markdownlint-cli2@0.8.1 '**/*.md' --config .markdownlint.yml
