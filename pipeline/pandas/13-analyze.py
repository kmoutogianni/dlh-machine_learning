#!/usr/bin/env python3
"""modeule 13"""


def analyze(df):
    """Computes descriptive statistics for all columns except
    the Timestamp column. Returns a new pd.DataFrame
    containing these statistics.
    """

    stats = df.drop(columns=["Timestamp"]).describe()
    return stats
