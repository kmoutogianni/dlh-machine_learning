#!/usr/bin/env python3
"""module 10"""


def index(df):
    """Sets the Timestamp column as the index of the dataframe"""
    return df.set_index("Timestamp")
