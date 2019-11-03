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
df=pd.read_csv('movies.csv')
columns_in_csv=['year', 'runtime']
# def print_table(table):
#     t = PrettyTable(table)
#     print(t)
def generate_data_from_api():
    whole_data = pd.DataFrame()
    for title in df['title']:
        print(title)
        url = serviceurl+change_space_to_plus(title)+apikey
       # print(url)
        response = urlopen(url)
        data = json.loads(response.read())
        # print(data)
        data_from_api=pd.DataFrame(data=data)
       # print(data_from_api)

        #for column in columns_in_csv:
        clear_data = data_from_api.filter(['Title', 'Year', 'Runtime', 'Genre', 'Director', 'Cast', 'Writer', 'Language', 'Country', 'Awards','imdbRating', 'imdbVotes', 'BoxOffice'], axis=1)
        clear_data = clear_data.iloc[0]
        whole_data = whole_data.append(clear_data)
    return whole_data

def save_to_csv(whole_data):
    filename = "movies_done.csv"
    f = open(filename, "w+")  ##clearing csv file        f.close()
    with open(filename, 'a') as f:
        whole_data.to_csv(f, header=True, index=True)
    #data = pd.read_csv("movies_done.csv", index_col=0)

def change_space_to_plus(title):
    return title.replace(' ', '+')
def sorting(category):
    with conn:
        c.execute("""SELECT * FROM movies_generated ORDER BY (?) ASC """,(str(category),))
        conn.commit()
        print(c.fetchall())
#class filterin
def filtering_director():
    with conn:
        c.execute("""SELECT Director FROM movies_generated """)
        conn.commit()
        print(c.fetchall())
def filtering_actor():
    with conn:
        c.execute("""SELECT Actor FROM movies_generated """)
        conn.commit()
        print(c.fetchall())
def movies_nominated_for_oscar_not_win():
    with conn:
        c.execute("""SELECT Title FROM movies_generated WHERE (Awards LIKE "Nominated for%"  AND Awards LIKE "%Oscar%" )""")
        conn.commit()
        print(c.fetchall())
def movies_won_80_percent():
    with conn:
        c.execute("""SELECT Title FROM movies_generated WHERE (Awards LIKE "Nominated for%"  AND Awards LIKE "%Oscar%" )""")
        conn.commit()
        print(c.fetchall())
def movies_earned_over_100_000_000():
    #convert boxx ofice
    with conn:
        c.execute("""SELECT Title FROM movies_generated WHERE Box_Office>100000000""")
        conn.commit()
        print(c.fetchall())
def movies_in_certain_language(lang):
    with conn:
        c.execute("""SELECT (Title, Language) FROM movies_generated WHERE Language=(str.(lang))""")
        conn.commit()
        print(c.fetchall())
#####
#class comparing


if __name__ == "__main__":

    # whole_data=generate_data_from_api()
    #
    #
    # print(whole_data)
    # whole_data.to_sql(con=conn, name='movies_generated', if_exists='replace')
    # save_to_csv(whole_data)

    parser = argparse.ArgumentParser()
    parser.add_argument('--sort_by', type=str,
                        help='type name of column by which you want to sort your table')
    #parser.add_argument('--y', type=float, default=1.0,
                   #     help='What is the second number?')
    #parser.add_argument('--operation', type=str, default='add',
                    #    help='What operation? Can choose add, sub, mul, or div')
    args = parser.parse_args()
  #  sys.stdout.write(str(sorting(column)))
    if args.sort_by != None:
        sorting(args)
    # elif args.show != None:
    #     show(args)
    # elif args.delete != None:
    #     delete(args)
    # elif args.copy != None:
    #     copy(args)
    # elif args.rename != None:
    #     rename(args)

    conn.commit()
    conn.close()
    # with open('/home/milo/Desktop/Backend/movies_done.csv', 'r') as f:
    #     reader = csv.reader(f)
    #     columns = next(reader)
    #     conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
    #     #query = 'insert into MyTable({0}) values ({1})'
    #     #query = query.format(','.join(columns), ','.join('?' * len(columns)))
    #     cursor = conn.cursor()
    #     print(reader)
    #     cursor.commit()
    #data.drop([Unnamed], axis=1)
    # setting first name as index column
    #data.set_index("Awards", inplace=True)
    # display
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
