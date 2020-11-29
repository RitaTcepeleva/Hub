from pathlib import Path
import os
import pandas as pd
import torch

from hub.geodesic import *
from hub.metrics import *

data_path = Path(os.getcwd()).parent / "data"


def get_df():
    na_air_df = pd.read_csv("data/na_airports.csv")
    hi_air_df = pd.read_csv("data/hi_airports.csv")
    pak_air_df = pd.read_csv("data/pak_airports.csv")
    bangla_air_df = pd.read_csv("data/bangla_airports.csv")
    na_air_df.drop(columns=["Unnamed: 0"], inplace=True)
    hi_air_df.drop(columns=["Unnamed: 0"], inplace=True)
    pak_air_df.drop(columns=["Unnamed: 0"], inplace=True)
    bangla_air_df.drop(columns=["Unnamed: 0"], inplace=True)
    df = pd.concat([na_air_df, hi_air_df, pak_air_df, bangla_air_df], ignore_index=True)

    return df, na_air_df, hi_air_df, pak_air_df, bangla_air_df

df, na_air_df, hi_air_df, pak_air_df, bangla_air_df = get_df()
points = Points(df)
print('lslls')
