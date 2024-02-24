import json
from src.fetcher import parse_repos
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
