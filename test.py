from pathlib import Path
import os
import pandas as pd
import torch
import requests
from bs4 import BeautifulSoup
import json

from hub.geodesic import *
from hub.metrics import *
from geo import *

hub = Point(75.53782, -29.131544)

'''data_path = Path(os.getcwd()).parent / "data"


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
print('lslls')'''

api_key = "c07526f63bee4d248b5e3ce31f9d3435"
api_path = f"https://api.opencagedata.com/geocode/v1/json"


def get_proper_api_path(place, api_key=api_key, api_path=api_path):
    return f"{api_path}?q={place}&key={api_key}"


def fetch_place(place, **params):
    path = get_proper_api_path(place, **params)
    res = requests.get(path)

    if res.status_code != 200:
        print(f"Cannot fetch {place}")
        raise ValueError

    return json.loads(res.content.decode("utf8"))

path = "https://en.wikipedia.org/wiki/List_of_the_busiest_airports_in_Pakistan"
res = requests.get(path)

html = res.content.decode("utf8")

soup = BeautifulSoup(html, "html")
rows = soup.find("table").find_all("tr")[1:]
airports = []

#idxs=(2, 3, 4, 5)
'''for row in rows:
    airports.append(parse_row(row, **params))'''

#NORTH AMERICA
'''passengers = 0
for row in rows:
    tds = row.find_all("td")
    passengers += int(str(tds[idxs[3]].contents[0]).replace(",", ""))

sum = 0
for row in rows:
    tds = row.find_all("td")
    country = tds[idxs[2]].find_all("a")[0]["title"]
    sum += int(str(tds[idxs[3]].contents[0]).replace(",", ""))/passengers

    if (country != 'Mexico') and (tds[idxs[1]].a.string != 'Honolulu'):
        airport = {
            "name": tds[idxs[0]].a.string,
            "city": tds[idxs[1]].a.string,
            "country": country,
            "passengers": int(str(tds[idxs[3]].contents[0]).replace(",", ""))/passengers
        }
        query = f"{airport['city']},{airport['country']}"
        res_json = fetch_place(query)["results"]
        coords = res_json[0]["geometry"]
        airport["lng"] = coords["lng"]
        airport["lat"] = coords["lat"]
        airports.append(airport)

na_dataframe = pd.DataFrame(airports)
na_dataframe.to_csv("data/north_america.csv")'''

#INDIA
'''idxs = (1, 2, 3, 5)
passengers = 0
for row in rows:
    tds = row.find_all("td")
    passengers += int(str(tds[idxs[3]].contents[0]).replace(",", ""))

sum = 0
for row in rows:
    tds = row.find_all("td")
    country = tds[idxs[2]].find_all("a")[0]["title"]
    sum += int(str(tds[idxs[3]].contents[0]).replace(",", ""))/passengers

    if country != 'Andaman and Nicobar Islands':
        airport = {
            "name": tds[idxs[0]].a.string,
            "city": tds[idxs[1]].a.string,
            "country": country,
            "passengers": int(str(tds[idxs[3]].contents[0]).replace(",", ""))/passengers
        }
        query = f"{airport['city']},{airport['country']}"
        res_json = fetch_place(query)["results"]
        coords = res_json[0]["geometry"]
        airport["lng"] = coords["lng"]
        airport["lat"] = coords["lat"]
        airports.append(airport)

hi_dataframe = pd.DataFrame(airports)
hi_dataframe.to_csv("data/india.csv")'''

#PAKISTAN

'''passengers = 0
for row in rows:
    tds = row.find_all("td")
    passengers += int(str(tds[idxs[3]].contents[0]).replace(",", ""))

sum = 0

for row in rows:
    tds = row.find_all("td")
    country = tds[idxs[2]].contents[0].rstrip()
    sum += int(str(tds[idxs[3]].contents[0]).replace(",", ""))/passengers
    airport = {
        "name": tds[idxs[0]].a.string,
        "city": tds[idxs[1]].a.string,
        "country": country,
        "passengers": int(str(tds[idxs[3]].contents[0]).replace(",", ""))/passengers
    }
    query = f"{airport['city']},{airport['country']}"
    res_json = fetch_place(query)["results"]
    if len(res_json) == 0:
        if (airport['city'] == 'Mohenjodaro'):
            query = 'Moenjodaro'
            res_json = fetch_place(query)["results"]
        elif (airport['city'] == 'Dalbadin'):
            query = 'Dalbandin,DBA'
            res_json = fetch_place(query)["results"]
    coords = res_json[0]["geometry"]
    airport["lng"] = coords["lng"]
    airport["lat"] = coords["lat"]
    airports.append(airport)

pak_dataframe = pd.DataFrame(airports)
pak_dataframe.to_csv("data/pakistan.csv")'''
#BANGLADESH
bangla_path = 'https://en.wikipedia.org/wiki/List_of_airports_in_Bangladesh'
res = requests.get(bangla_path)
html = res.content.decode("utf8")
soup = BeautifulSoup(html, "html")
airports = []
rows = soup.find_all("table")
idxs = (1,0,3,6)
narod = 0
for i in range(3,10):
    tds = rows[i].find_all("td")
    length = int(len(tds)/7)
    if length == 8:
        length = 2
    for j in range(length):
        k0 = j*7;
        if (tds[2+k0].contents[0].rstrip() != '—' and tds[3+k0].contents[0].rstrip() != '—'):
            if (tds[4+k0].contents[0].rstrip() == 'International' or tds[4+k0].contents[0].rstrip() == 'Domestic'):
                href = 'https://en.wikipedia.org/'+tds[1+k0].contents[0].attrs['href']
                res1 = requests.get(href)
                html1 = res1.content.decode('utf8')
                soup1 = BeautifulSoup(html1,'html')
                rows1 = soup1.find("table").find_all("tr")[1:]
                passengers = rows1[len(rows1)-2].contents[1].text
                narod += int(str(passengers).replace(",", ""))

sum = 0
for i in range(3,10):
    tds = rows[i].find_all("td")
    length = int(len(tds)/7)
    if length == 8:
        length = 2
    for j in range(length):
        k0 = j*7;
        if (tds[2+k0].contents[0].rstrip() != '—' and tds[3+k0].contents[0].rstrip() != '—'):
            if (tds[4+k0].contents[0].rstrip() == 'International' or tds[4+k0].contents[0].rstrip() == 'Domestic'):
                href = 'https://en.wikipedia.org/'+tds[1+k0].contents[0].attrs['href']
                res1 = requests.get(href)
                html1 = res1.content.decode('utf8')
                soup1 = BeautifulSoup(html1,'html')
                rows1 = soup1.find("table").find_all("tr")[1:]
                passengers = rows1[len(rows1)-2].contents[1].text
                airport = {
                    "name": tds[idxs[0]+k0].a.string,
                    "city": tds[idxs[1]+k0].a.string,
                    "country": tds[idxs[2]+k0].contents[0].rstrip(),
                    "passengers": int(str(passengers).replace(",", ""))/narod
                }
                sum += int(str(passengers).replace(",", ""))/narod
                query = f"{airport['city']},{airport['country']}"
                res_json = fetch_place(query)["results"]
                coords = res_json[0]["geometry"]
                airport["lng"] = coords["lng"]
                airport["lat"] = coords["lat"]
                airports.append(airport)

bangla_dataframe = pd.DataFrame(airports)
bangla_dataframe.to_csv("data/bangladesh.csv")
#print(sum)
