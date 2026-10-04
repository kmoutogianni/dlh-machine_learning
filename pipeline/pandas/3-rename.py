#!/usr/bin/env python3
"""Pandas module 3"""
import pandas as pd


def rename(df):
    """rename and change to datetime"""
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"])
    return df[["Datetime", "Close"]]
