#!/usr/bin/env python3
"""Pandas module 8"""


def prune(df):
    """Removes any entries where Close has NaN values"""
    return df.dropna(subset=["Close"])
