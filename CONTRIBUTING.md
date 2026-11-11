# Contributing

- Every change starts from an issue.
- Branch: `type/<issue>-short-desc`, e.g. `feat/12-router-rules`.
- Commits: Conventional Commits (`feat|fix|test|docs|chore|perf|refactor|ci: ...`).
- PR: fill the template, link `Closes #N`, squash merge, CI must be green.
- Secrets only in `.env` (git-ignored) and GitHub Secrets. Run `pre-commit install` once.
- Major tech choices go in an ADR under `docs/adr/`.
