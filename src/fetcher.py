import requests_cache
from urllib.parse import urlparse, parse_qs, urlunparse, urlencode

BASE_URL = "https://api.github.com"

# Notes about the github API:
# - The API is rate limited to 60 requests per hour for unauthenticated requests
# - The API is rate limited to 5000 requests per hour for authenticated requests
# - It's paginated. Max value for `per_page` is 100. The `Link` header contains links to different pages relative to the current page See: https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api?apiVersion=2022-11-28


class Fetcher:
    """Fetch info from the GitHub API"""

    session = requests_cache.CachedSession(
        "github_cache", use_cache_dir=True, cache_control=True
    )

    def fetch_repos(self, username: str) -> list[str]:
        """Fetch the repositories for a given user"""
        items = self.__fetch_paginated(f"/users/{username}/repos")
        return parse_repos(items)

    def fetch_commit_count(self, username: str, repo: str) -> int:
        """Fetch the number of commits for a given user and repository"""
        # HACK: To save on requests, we're only fetching the first page with one commit per page.
        # Then we can count the number of commits by looking at the `Link` header in the response
        resp = self.session.get(
            f"{BASE_URL}/repos/{username}/{repo}/commits?per_page=1"
        )
        resp.raise_for_status()
        link_header = resp.headers.get("Link")
        if link_header is None:
            raise ValueError("Link header not found in response")
        links = parse_link_header(link_header)
        last = urlparse(links["last"])
        query = parse_qs(last.query)
        return int(query["page"][0])

    def __fetch_paginated(self, url: str) -> list[dict]:
        """Fetch a paginated resource from the GitHub API and return all the results"""
        assert url.startswith("/")
        parsed = urlparse(f"{BASE_URL}{url}")
        query = parse_qs(parsed.query)
        query["per_page"] = ["100"]
        has_next = True
        page = 1
        items: list[dict] = []

        while has_next:
            query["page"] = [str(page)]
            new_url = urlunparse(parsed._replace(query=urlencode(query, doseq=True)))
            print(f"fetching {new_url}")
            resp = self.session.get(new_url)
            resp.raise_for_status()
            items.extend(resp.json())

            has_next = "next" in resp.headers.get("Link", "")
            page += 1

        return items


def parse_link_header(link_header: str) -> dict[str, str]:
    """Parse the `Link` header from a GitHub API response into a dictionary"""
    # TODO: implement
    return {
        "last": "https://api.github.com/repositories/198065251/commits?per_page=1&page=3095"
    }


def parse_repos(raw: list[dict]) -> list[str]:
    """Parse the raw JSON response from the GitHub API into a list of repository names"""
    return [repo["name"] for repo in raw]
