# GitHubApi567

[![CI](https://github.com/ssw-567-group-work/GitHubApi567/actions/workflows/ci.yml/badge.svg?event=push)](https://github.com/ssw-567-group-work/GitHubApi567/actions/workflows/ci.yml)

## Setup

1. Install Python 3.10 or later
2. Install [poetry](https://python-poetry.org/docs/#installing)
3. Install [just](https://github.com/casey/just#installation)
4. Install github cli (different from `git`)
5. Clone the repository
6. Install dependencies
```bash
poetry install
```

## Developing

Use `poetry run python3 <file>` to execute a file with the virtual environment.

Run lints
```bash
just lint
```

Run tests
```bash
just test
```

### Making PRs

1. Create a branch
```bash
git checkout -b <branch-name>
```
2. Make changes and commit them
3. Create the PR
```bash
gh pr create
```
