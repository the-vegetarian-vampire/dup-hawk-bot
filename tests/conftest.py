import os
from pathlib import Path

import pandas as pd
import pytest

from dup_hawk import Github

# Define the path to the current file
current_file_path = Path(__file__)
data_directory = current_file_path.parent / "test_data"
# Define the paths to the pickle files
df_path = data_directory / "df.pkl"
dist_df_path = data_directory / "dist_df.pkl"


@pytest.fixture
def pat_token():
    return os.getenv("GITHUB_PAT_TOKEN")


@pytest.fixture
def df():
    return pd.read_pickle(df_path)


@pytest.fixture
def dist_df():
    return pd.read_pickle(dist_df_path)
