#!/usr/bin/env python3
"""Pandas module 2"""
import pandas as pd


def from_file(filename, delimiter):
    """loads data from a file as a pd.DataFrame"""
    return pd.read_csv(filename, delimiter=delimiter)
