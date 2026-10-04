#!/usr/bin/env python3
"""modeule 12"""
import pandas as pd

def hierarchy(df1, df2):
    """builds on the the previous one, and rearranges the indexes"""
    index = __import__('10-index').index

    df1 = index(df1)
    df2 = index(df2)

    df1 = df1.loc[1417411980:1417417980]
    df2 = df2.loc[1417411980:1417417980]

    df = pd.concat([df2, df1], keys=["bitstamp", "coinbase"])

    df = df.swaplevel(0, 1)
    return df.sort_index()
