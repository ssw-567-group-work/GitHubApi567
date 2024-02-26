import requests_mock
import pytest
import requests

from src.fetcher import Fetcher


def build_mocks(session):
    m = requests_mock.Mocker(session=session, real_http=False)
    m.get(
        "https://api.github.com/users/dyc3/repos",
        json=[
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ],
    )
    m.get(
        "https://api.github.com/repos/dyc3/repo1/commits?per_page=1",
        headers={
            "Link": '<https://api.github.com/repositories/198065251/commits?per_page=1&page=6>; rel="last"'
        },
    )
    m.get(
        "https://api.github.com/repos/dyc3/repo2/commits?per_page=1",
        headers={
            "Link": '<https://api.github.com/repositories/198065251/commits?per_page=1&page=8>; rel="last"'
        },
    )
    m.get(
        "https://api.github.com/repos/dyc3/repo3/commits?per_page=1",
        headers={
            "Link": '<https://api.github.com/repositories/198065251/commits?per_page=1&page=26>; rel="last"'
        },
    )

    m.get(
        "https://api.github.com/users/fake/repos?page=1",
        json=[
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ],
        headers={
            "Link": '<https://api.github.com/users/fake/repos?per_page=100&page=2>; rel="next"'
        },
    )
    m.get(
        "https://api.github.com/users/fake/repos?page=2",
        json=[
            {"name": "repo4"},
            {"name": "repo5"},
            {"name": "repo6"},
        ],
    )

    m.get("https://api.github.com/repos/nolink/repo1/commits?per_page=1", json=[])

    return m


def test_fetch_repos():
    fetcher = Fetcher()
    fetcher.session = requests.Session()
    with build_mocks(fetcher.session) as m:
        repos = fetcher.fetch_repos("dyc3")
        assert repos == ["repo1", "repo2", "repo3"]


def test_fetch_repos_multi_page():
    fetcher = Fetcher()
    fetcher.session = requests.Session()
    with build_mocks(fetcher.session) as m:
        repos = fetcher.fetch_repos("fake")
        assert repos == ["repo1", "repo2", "repo3", "repo4", "repo5", "repo6"]


@pytest.mark.skip(reason="not implemented")
def test_fetch_commit_count():
    fetcher = Fetcher()
    fetcher.session = requests.Session()
    with build_mocks(fetcher.session) as m:
        count = fetcher.fetch_commit_count("dyc3", "repo1")
        assert count == 6


def test_fetch_commit_count_no_link():
    fetcher = Fetcher()
    fetcher.session = requests.Session()
    with build_mocks(fetcher.session) as m:
        with pytest.raises(ValueError):
            fetcher.fetch_commit_count("nolink", "repo1")
