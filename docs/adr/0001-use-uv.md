# ADR-0001: Use uv for Python version, environment and dependency management

- Status: accepted
- Date: 2026-11-11

## Context
We need reproducible installs across WSL dev, CI (GitHub Actions) and Docker, with a lockfile.

## Options
1. **uv** — one tool for Python versions, venv and deps; fast; cross-platform `uv.lock`; good Docker/CI support. Younger project, CLI still evolving.
2. **Poetry** — mature, widely documented. Slower resolves/installs; Python versions managed separately (pyenv).

## Decision
uv. Speed matters in CI and Docker builds, and one tool replaces pyenv + venv + pip.

## Consequences
- Contributors install uv once; all commands run via `uv run`.
- `uv.lock` is committed and must be updated through `uv add` / `uv lock`, never edited by hand.
