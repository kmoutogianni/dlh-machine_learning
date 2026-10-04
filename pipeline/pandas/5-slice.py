#!/usr/bin/env python3
"""Pandas module 5"""


def slice(df):
    """extracts columns and selects every 60th row from these columns"""
    extracted = df[["High", "Low", "Close", "Volume_(BTC)"]]
    selected = extracted.iloc[::60]  # start, stop, STEP (60)
    return selected
