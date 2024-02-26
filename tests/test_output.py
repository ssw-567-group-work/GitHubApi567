import pytest
import src
from src.fetcher import Fetcher


class MockFetcher(Fetcher):
    def fetch_repos(self, username):
        return [
            "repo1",
            "repo2",
            "repo3",
        ]

    def fetch_commit_count(self, username, repo):
        return 10


def test_output(capfd):
    src.main(["goober"], fetcher=MockFetcher())
    out, err = capfd.readouterr()
    assert (
        out
        == "Repo: repo1 Number of commits: 10\nRepo: repo2 Number of commits: 10\nRepo: repo3 Number of commits: 10\n"
    )
