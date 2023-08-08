import os

import pytest

from dup_hawk import Github

TEST_REPO = "https://github.com/Cyfrin/foundry-defi-stablecoin-f23"
PRIVATE_REPO = "https://github.com/PatrickAlphaC/actions-app-test"
BIG_REPO = "https://github.com/Cyfrin/2023-07-foundry-defi-stablecoin"


@pytest.mark.integration
def test_get_user(pat_token):
    g = Github(pat_token)
    user = g.get_user()
    assert user["login"] is not None


@pytest.mark.integration
def test_get_repo(pat_token):
    g = Github(pat_token)
    repo = g.get_repo(TEST_REPO)
    assert repo["id"] is not None


@pytest.mark.integration
def test_get_issues(pat_token):
    g = Github(pat_token)
    issues = g.get_issues(TEST_REPO)
    assert isinstance(issues, list)


@pytest.mark.integration
def test_get_many_issues(pat_token):
    g = Github(pat_token)
    issues = g.get_issues(BIG_REPO)
    assert len(issues) > 1000
    assert isinstance(issues, list)


@pytest.mark.integration
def test_get_private_issues(pat_token):
    g = Github(pat_token)
    issues = g.get_issues(PRIVATE_REPO)
    assert isinstance(issues, list)


@pytest.mark.integration
def test_label_issue(pat_token):
    label_name = "ai-duplicate"
    g = Github(pat_token)
    issues = g.get_issues(PRIVATE_REPO)
    issue_number = issues[0]["number"]
    response = g.tag_issue(issue_number, PRIVATE_REPO, [label_name])
    assert response[0]["name"] == label_name
