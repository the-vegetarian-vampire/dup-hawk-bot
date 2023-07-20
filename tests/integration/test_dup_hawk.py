import os

import pytest

from dup_hawk import mark_duplicates

PAT_TOKEN = os.getenv("GITHUB_PAT_TOKEN")
GIT_REPO_URL = "https://github.com/PatrickAlphaC/actions-app-test"


@pytest.mark.integration
def test_mark_issue():
    mark_duplicates(GIT_REPO_URL, PAT_TOKEN)
