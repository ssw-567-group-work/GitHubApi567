import json
from src.fetcher import parse_repos, parse_link_header
from . import read_fixture


def test_parse_repos():
    raw = [
        {"name": "repo1"},
        {"name": "repo2"},
        {"name": "repo3"},
    ]
    assert parse_repos(raw) == ["repo1", "repo2", "repo3"]


def test_parse_repos_fixture():
    fixture = read_fixture("repos-list-1.json")
    data = json.loads(fixture)
    assert parse_repos(data) == [
        "d6-survey-service",
        "opentogethertube",
        "steamguard-cli",
    ]


def test_parse_link_headers():
    link_header = (
        '<https://api.github.com/repositories/198065251/commits?per_page=1&page=3095>; rel="last", '
        '<https://api.github.com/repositories/198065251/commits?per_page=1&page=2>; rel="next", '
        '<https://api.github.com/repositories/198065251/commits?per_page=1&page=1>; rel="first", '
        '<https://api.github.com/repositories/198065251/commits?per_page=1&page=3093>; rel="prev"'
    )
    assert parse_link_header(link_header) == {
        "last": "https://api.github.com/repositories/198065251/commits?per_page=1&page=3095",
        "next": "https://api.github.com/repositories/198065251/commits?per_page=1&page=2",
        "first": "https://api.github.com/repositories/198065251/commits?per_page=1&page=1",
        "prev": "https://api.github.com/repositories/198065251/commits?per_page=1&page=3093",
    }
    link_header = (
        '<https://api.github.com/repositories/198065251/commits?per_page=1&page=3095>; rel="last", '
        '<https://api.github.com/repositories/198065251/commits?per_page=1&page=2>; rel="next", '
        '<https://api.github.com/repositories/198065251/commits?per_page=1&page=1>; rel="first"'
    )
    assert parse_link_header(link_header) == {
        "last": "https://api.github.com/repositories/198065251/commits?per_page=1&page=3095",
        "next": "https://api.github.com/repositories/198065251/commits?per_page=1&page=2",
        "first": "https://api.github.com/repositories/198065251/commits?per_page=1&page=1",
    }
