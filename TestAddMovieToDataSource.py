import pandas as pd
import requests
import time
from bs4 import BeautifulSoup
import argparse
import sys
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import json
import csv
import sqlite3
import sys
import getopt

#df = pd.read_csv
#for title in df['title']:
from prettytable import PrettyTable
#url = 'http://www.omdbapi.com/?t=The+Shawshank+Redemption&apikey=ccfc0898'
#url = 'http://web.mta.info/developers/turnstile.html'
#response = requests.get(url)
conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
c = conn.cursor()
serviceurl = 'http://www.omdbapi.com/?t='
apikey = '&apikey='+'ccfc0898'
df=pd.read_csv('/home/milo/Desktop/Backend/movies.csv')


def change_space_to_plus(title):
    return title.replace(' ', '+')
####################################################################################################################################################
title="Kac Wawa"
url = serviceurl + change_space_to_plus(title) + apikey
response = urlopen(url)
data = json.loads(response.read())
# print(data)
data_from_api = pd.DataFrame(data=data)
# print(data_from_api)

# for column in columns_in_csv:
clear_data = data_from_api.filter(['Title', 'Year', 'Runtime', 'Genre', 'Director', 'Actors', 'Writer', 'Language', 'Country', 'Awards','imdbRating', 'imdbVotes', 'BoxOffice'], axis=1)
clear_data = clear_data.iloc[0]
print(type(clear_data))
clear_data.dropna(how='all')
print(clear_data)
clear_data.to_sql(con=conn, name='movies_generated', if_exists='append')
print(c.fetchall())
# comm = "INSERT INTO movies_generated VALUES( '"
# for x in clear_data:
#     comm = comm + x + "', '"
# comm = comm + "')"
# print(comm)
# c.execute(comm);
