from unittest.mock import patch
import pandas as pd
import pytest
from dup_hawk import mark_duplicates_from_dfs

#  TO RUN: pytest test_dup_hawk.py

# Sample data as pytest fixtures


@pytest.fixture
def sample_df():
    # Replace with data
    data = {
        'number': [1, 2, 3],
        'title': ["Issue 1", "Issue 2", "Issue 3"],
        'body': ["Description 1", "Description 2", "Description 3"]
    }
    return pd.DataFrame(data)


@pytest.fixture
def sample_dist_df():
    # Replace with data
    data = {
        # Your distance data here
    }
    return pd.DataFrame(data)


def test_mark_duplicates_from_dfs(sample_df, sample_dist_df):
    response = mark_duplicates_from_dfs(sample_df, sample_dist_df)
    assert response == {3: [2], 2: [3]}
