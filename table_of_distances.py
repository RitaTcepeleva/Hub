import os
from pathlib import Path

import pandas as pd
import torch

from hub.geodesic import *
from hub.metrics import *
from geo import *

#hub = torch.tensor([75.424385, -29.941536])

hub = Point(75.53782, -29.131544)
'''airports = []
#NA
airports.append(Point(45.4972159, -73.6103642))
airports.append(Point(29.9499323, -90.0701156))
airports.append(Point(21.304547, -157.8556764))
#INDIA
airports.append(Point(34.1642029, 77.5848133))
airports.append(Point(19.7668121, 74.4754386))
airports.append(Point(11.6645348, 92.7390448))
#PAKISTAN
airports.append(Point(24.900819, 67.1594188))
airports.append(Point(35.8877664, 71.8007275))
airports.append(Point(28.8759393, 64.401426))
#BANGLADESH
airports.append(Point(22.8040204, 90.3006337))
airports.append(Point(24.9640011, 91.8610944))
airports.append(Point(25.7579503, 88.9094267))

i = 0
for airport in airports:
    if i < 3:
        print('NA')
        print(distance(hub, airport))
    elif 2<i<6:
        print('INDIA')
        print(distance(hub, airport))
    elif 5<i<9:
        print('PAKISTAN')
        print(distance(hub, airport))
    else:
        print('BANGLADESH')
        print(distance(hub, airport))
    i = i + 1'''

objects = []
def get_df():
    na_air_df = pd.read_csv("data/north_america.csv")
    hi_air_df = pd.read_csv("data/india.csv")
    pak_air_df = pd.read_csv("data/pakistan.csv")
    bangla_air_df = pd.read_csv("data/bangladesh.csv")
    na_air_df.drop(columns=["Unnamed: 0"], inplace=True)
    hi_air_df.drop(columns=["Unnamed: 0"], inplace=True)
    pak_air_df.drop(columns=["Unnamed: 0"], inplace=True)
    bangla_air_df.drop(columns=["Unnamed: 0"], inplace=True)
    df = pd.concat([na_air_df, hi_air_df, pak_air_df, bangla_air_df], ignore_index=True)

    return df, na_air_df, hi_air_df, pak_air_df, bangla_air_df


df, na_air_df, hi_air_df, pak_air_df, bangla_air_df = get_df()
points = Points(df)
'''for i in range(len(points['airports']['values']['array'])):
    point = Point(points['airports']['values']['array'][i]['array'][5], points['airports']['values']['array'][i]['array'][4])
    object = {
            "name": points['airports']['values']['array'][i]['array'][0],
            "city": points['airports']['values']['array'][i]['array'][1],
            "country": points['airports']['values']['array'][i]['array'][2],
            "passengers": points['airports']['values']['array'][i]['array'][3],
            "distance": distance(hub, point)
        }
    objects.append(object)'''

for airpot in points.airports.values:
    #point = airpot.values.array
    point = Point(float(airpot[5]), float(airpot[4]))
    object = {
        "name": airpot[0],
        "city": airpot[1],
        "country": airpot[2],
        "passengers": airpot[3],
        "distance": distance(hub, point)
    }
    objects.append(object)

dataframe = pd.DataFrame(objects)
dataframe.to_csv("data/table_of_distances.csv")
