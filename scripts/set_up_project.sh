#!/bin/sh
set -ex
git config --local core.commentChar ";"  # Allow commit messages to start with hash (#).
uv sync --group dev
uv run pre-commit install --install-hooks
