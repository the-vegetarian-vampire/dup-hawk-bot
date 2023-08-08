import os

import pytest

from dup_hawk import create_embeddings_and_dfs, dup_hawk
from tests.test_data.data import repo_issues

PAT_TOKEN = os.getenv("GITHUB_PAT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GIT_REPO_URL = "https://github.com/PatrickAlphaC/actions-app-test"
GIT_REPO_URL_TWO = "https://github.com/Cyfrin/2023-07-foundry-defi-stablecoin"
SIMILARITY_THRESHOLD_DEFAULT = 0.85


@pytest.mark.integration
def test_dup_hawk_full():
    dup_hawk(GIT_REPO_URL, PAT_TOKEN, OPENAI_API_KEY, SIMILARITY_THRESHOLD_DEFAULT)


@pytest.mark.integration
def test_create_embeddings_and_dfs():
    create_embeddings_and_dfs(repo_issues)


@pytest.mark.integration
def test_dup_hawk_full_two():
    dup_hawk(GIT_REPO_URL_TWO, PAT_TOKEN, OPENAI_API_KEY, SIMILARITY_THRESHOLD_DEFAULT)
