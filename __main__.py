import pandas as pd
import requests
import time
from bs4 import BeautifulSoup

import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import json
import csv
#df = pd.read_csv
#for title in df['title']:

#url = 'http://www.omdbapi.com/?t=The+Shawshank+Redemption&apikey=ccfc0898'
#url = 'http://web.mta.info/developers/turnstile.html'
#response = requests.get(url)

serviceurl = 'http://www.omdbapi.com/?t='
apikey = '&apikey='+'ccfc0898'
df=pd.read_csv('movies.csv')
columns_in_csv=['year', 'runtime']
whole_data=pd.DataFrame()
def change_space_to_plus(title):
    return title.replace(' ', '+')
if __name__ == "__main__":
    for title in df['title']:
        print(title)
        url = serviceurl+change_space_to_plus(title)+apikey
        print(url)
        response = urlopen(url)
        data = json.loads(response.read())
        # print(data)
        data_from_api=pd.DataFrame(data=data)
        print(data_from_api)

        #for column in columns_in_csv:

        clear_data=data_from_api.filter(['Title', 'Year', 'Runtime', 'Genre', 'Director', 'Cast', 'Writer', 'Language', 'Country', 'Awards','imbdRating', 'imbdVotes', 'BoxOffice'], axis=1)
        clear_data=clear_data.iloc[0]
        clear_data.tolist()
        clear_data = clear_data[::-1]
        print(clear_data)

        print(clear_data.shape)
        whole_data=whole_data.append(clear_data)
        print(whole_data)
        # list_values = [value for value in clear_data.values()]
        # print(list_values)
        if title=='Gone Girl':
            break
    with open('movies_helping.csv', 'a') as f:
        whole_data.to_csv(f, header=False)
    df_check=pd.read_csv('movies_helping.csv')
    print(df_check)
            # thewriter = csv.writer(f)
            # thewriter.writerow([clear_data)
        #
        # if k in list(clear_data):
        #     print(f"{k}: {json_data[k]}")





def print_json(json_data):
    list_keys=['Title', 'Year', 'Runtime', 'Genre', 'Director', 'Cast', 'Writer', 'Language', 'Country', 'Awards','imbdRating', 'imbdVotes', 'BoxOffice']
    print("-"*50)
    for k in list_keys:
        if k in list(json_data.keys()):
            print(f"{k}: {json_data[k]}")
    print("-"*50)
def add_to_csv(json_data):
    Csv_keys = ['Title', 'Year', 'Runtime', 'Genre', 'Director', 'Cast', 'Writer', 'Language', 'Country', 'Awards',
                 'imbdRating', 'imbdVotes', 'BoxOffice']
    for k in Csv_keys:
        df['k']


#from omdbapi.movie_search import GetMovie
#omdb.set_default('apikey', ccfc0898)
#movie = GetMovie(title='Interstellar', api_key='ccfc0898')

from pymatgen.ext.matproj import MPRester

#movie.get_all_data('Year', 'Runtime', 'Genre', 'Director', 'Cast', 'Writer', 'Language', 'Country', 'Awards','imbdRating', 'imbdVotes', 'BoxOffice')

#if __name__ =='__main__':
 #   MAPI_KEY=ccfc0898
