#!/usr/bin/env python3
"""Pandas module 4"""


def array(df):
    """processes the df and returns an np array"""
    selected = df[['High', 'Close']].tail(10)
    return selected.to_numpy()
