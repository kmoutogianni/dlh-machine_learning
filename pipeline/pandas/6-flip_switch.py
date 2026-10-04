#!/usr/bin/env python3
"""Pandas module 6"""


def flip_switch(df):
    """Sorts the data in reverse chronological order
    and transposes the sorted dataframe"""
    df = df.sort_index(ascending=False)
    return df.T
