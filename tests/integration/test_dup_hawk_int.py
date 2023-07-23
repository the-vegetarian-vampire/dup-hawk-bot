import os

import pytest

from dup_hawk import create_embeddings_and_dfs, dup_hawk
from tests.test_data.data import repo_issues

PAT_TOKEN = os.getenv("GITHUB_PAT_TOKEN")
GIT_REPO_URL = "https://github.com/PatrickAlphaC/actions-app-test"


@pytest.mark.integration
def test_dup_hawk_full():
    dup_hawk(GIT_REPO_URL, PAT_TOKEN)


@pytest.mark.integration
def test_create_embeddings_and_dfs():
    create_embeddings_and_dfs(repo_issues)
