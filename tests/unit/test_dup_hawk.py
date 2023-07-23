import pandas as pd

from dup_hawk import mark_duplicates_from_dfs


def test_mark_duplicates_from_dfs(df, dist_df):
    response = mark_duplicates_from_dfs(df, dist_df)
    assert response == {3: [2], 2: [3]}
