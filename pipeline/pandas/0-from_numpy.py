#!/usr/bin/env python3
"""Pandas module 0"""
import pandas as pd


def from_numpy(array):
    """creates a pd.DataFrame from a np.ndarray"""
    alph_columns = [chr(65 + i) for i in range(array.shape[1])]
    df = pd.DataFrame(array, columns=alph_columns)
    return(df)
