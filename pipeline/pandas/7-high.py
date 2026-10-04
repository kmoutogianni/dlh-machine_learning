#!/usr/bin/env python3
"""Pandas module 6"""


def high(df):
    """sorts dataframe values"""
    sorted_df = df.sort_values("High", ascending=False)
    return sorted_df
