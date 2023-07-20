import os

import pytest

from pygithub import Github

PAT_TOKEN = os.getenv("GITHUB_PAT_TOKEN")
TEST_REPO = "https://github.com/smartcontractkit/chainlink"
PRIVATE_REPO = "https://github.com/PatrickAlphaC/actions-app-test"


@pytest.mark.integration
def test_get_user():
    g = Github(PAT_TOKEN)
    user = g.get_user()
    assert user["login"] is not None


@pytest.mark.integration
def test_get_repo():
    g = Github(PAT_TOKEN)
    repo = g.get_repo(TEST_REPO)
    assert repo["id"] is not None


@pytest.mark.integration
def test_get_issues():
    g = Github(PAT_TOKEN)
    issues = g.get_issues(TEST_REPO)
    assert isinstance(issues, list)


@pytest.mark.integration
def test_get_private_issues():
    g = Github(PAT_TOKEN)
    issues = g.get_issues(PRIVATE_REPO)
    assert isinstance(issues, list)
