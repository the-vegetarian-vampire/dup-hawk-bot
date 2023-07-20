from typing import Optional
from urllib.parse import urlparse

import requests

BASE_URL = "https://api.github.com/"
X_GITHUB_API_VERSION = "2022-11-28"
HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": "token ",
    "X-GitHub-Api-Version": X_GITHUB_API_VERSION,
}


class Github:
    def __init__(self, token: str):
        self.token = token
        self.headers = HEADERS
        self.headers["Authorization"] = f"token {self.token}"
        self.url = BASE_URL

    def get_user(self) -> dict:
        url = self.url + "user"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_repo(self, repo_url: str) -> dict:
        owner, repo = self.get_owner_and_repo(repo_url)
        url = self.url + f"repos/{owner}/{repo}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_issues(self, repo_url: str, state: Optional[str] = "open") -> dict:
        """
        Gets a list of issues for a given repo.

        Args:
            repo_url (str): The repo to get issues from
            state (str, optional): Can be one of [open, closed, all]. Defaults to open.

        Returns:
            dict: _description_
        """
        owner, repo = self.get_owner_and_repo(repo_url)
        url = self.url + f"repos/{owner}/{repo}/issues"
        params = {"state": state}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    @staticmethod
    def get_owner_and_repo(url: str) -> tuple[str, str]:
        parsed_url = urlparse(url)
        path = parsed_url.path
        owner, repo = path.strip("/").split("/")[0:2]
        return owner, repo