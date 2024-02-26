from typing import Sequence
from .cli import Args
from .fetcher import Fetcher


def main(argv: Sequence[str] | None = None, fetcher: Fetcher = Fetcher()):
    args = Args(underscores_to_dashes=True).parse_args(argv)
    repos = fetcher.fetch_repos(args.username)
    for repo in repos:
        commits = fetcher.fetch_commit_count(args.username, repo)
        print(f"Repo: {repo} Number of commits: {commits}")


def add(a, b):
    return a + b
