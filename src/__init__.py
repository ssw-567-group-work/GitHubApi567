from .cli import Args
from .fetcher import Fetcher


def main():
    args = Args(underscores_to_dashes=True).parse_args()
    fetcher = Fetcher()
    repos = fetcher.fetch_repos(args.username)
    commits = fetcher.fetch_commit_count(args.username, repos[0])
    print(repos)
    # TODO: implement


def add(a, b):
    return a + b
