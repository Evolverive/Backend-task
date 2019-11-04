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
df=pd.read_csv('movies.csv')
columns_in_csv=['year', 'runtime']
# def print_table(table):
#     t = PrettyTable(table)
#     print(t)
def sorting(category, table_n):
    with conn:
        # cur.execute('SELECT * FROM tab = :tab ORDER BY cat = :cat ASC', {'tab':table_n, 'cat':category})
        c.execute('SELECT * FROM {} ORDER BY {} ASC'.format(table_n, category))
        conn.commit()
    for row in c:
        print(row)
def filter_by():
    start_date = None
    end_date = None

    # first argument is the filename with an index of 0
    # so, we want to start with an index value of 1
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "s:e:", ["start_date=", "end_date="])
    except getopt.GetoptError as err:
        print(err)  # will print something like "option -a not recognized"

    for opt, arg in opts:
        if opt in ["-s", "--start_date"]:
            start_date = arg
        elif opt in ["-e", "--end_date"]:
            end_date = arg

    print('start_date: {}'.format(start_date))
    print('end_date: {}'.format(end_date))
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
# def remove_zero_column():
#     with conn:
#         c.executescript("""BEGIN TRANSACTION;
# CREATE TEMPORARY TABLE movies_generated_backup(Title, Year, Runtime, Genre, Director, Writer, Language, Country, Awards, imdbRating, imdbVotes, BoxOffice);
# INSERT INTO movies_generated_backup SELECT Title, Year, Runtime, Genre, Director, Writer, Language, Country, Awards, imdbRating, imdbVotes, BoxOffice FROM movies_generated;
# DROP TABLE movies_generated;
# CREATE TABLE movies_generated(Title, Year, Runtime, Genre, Director, Writer, Language, Country, Awards, imdbRating, imdbVotes, BoxOffice);``
# INSERT INTO movies_generated SELECT Title, Year, Runtime, Genre, Director, Writer, Language, Country, Awards, imdbRating, imdbVotes, BoxOffice FROM movies_generated_backup;
# DROP TABLE movies_generated_backup""")
#         conn.commit()
#         print(c.fetchall())

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
def movies_that_won_over_80_percent():
    List_of_winners = []
    with conn:
        c.execute("""SELECT Awards, Title FROM movies_generated""")
        for row in c:
            Title = list(row)[1]
            #print(Title)
            nomination1 = re.findall(r'(\d+.?\d*) nominations', str(row))
            nomination2 = re.findall(r'Nominated for (\d+.?\d*)', str(row))
            win1 = re.findall(r'(\d+.?\d*) wins', str(row))
            win2 = re.findall(r'Won (\d+.?\d*)', str(row))
            if len(nomination1) == 0:
                nomination1.append(0)
            if len(nomination2) == 0:
                nomination2.append(0)
            if len(win1) == 0:
                win1.append(0)
            if len(win2) == 0:
                win2.append(0)
            all_nom = int(nomination1[0]) + int(nomination2[0])
            all_win = int(win1[0]) + int(win2[0])
            if (all_win + all_nom > 0):
                percent = (100 * all_win / (all_win + all_nom))
            else:
                percent = 0
            if percent > 80:
                Winner = "has won more than 80% of nominations with percent of"
                List_of_winners.append([Title, Winner, percent])
            # c.execute("INSERT INTO movies_generated(percent) VALUES {}".format())
            #print(" nominations : %s,%s , wins : %s, %s" % (nomination1, nomination2, win1, win2))
            #print("nom= %s , wins=%s" % (all_nom, all_win))
        conn.commit()
        print(List_of_winners)
def movies_earned_over_100_000_000():
    List_of_winners = []
    earned = 0
    Winner = "Has earned over 100 000 000 $ and the money is "
    with conn:
        c.execute("""SELECT BoxOffice, Title FROM movies_generated""")
        for row in c:
            Title = list(row)[1]
            Money = list(row)[0]
            # print(Money)


            if (Money != 'N/A' and Money != None):
                earned = re.findall(r'(\d+.?\d\d+.?\d *\d+.?\d *) *', Money)
                earned = int(earned[0].replace(',', ''))
            print(earned)
            if earned > 100000000:
                List_of_winners.append([Title, Winner, earned])
    print(List_of_winners)

def movies_in_certain_language(lang):
    with conn:
        c.execute("""SELECT (Title, Language) FROM movies_generated WHERE Language=(str.(lang))""")
        conn.commit()
        print(c.fetchall())
def compare_by_imbd_rating(Title2,Title1):
    column=imdbRating
    with conn:
        c.execute(
            "SELECT Title, " + column + " FROM movies_generated  WHERE Title='" + Title2 + "' OR Title='" + Title1 + "'")
        # c.execute()
        vars = []
        titles = []
        for row in c:
            titles.append(list(row)[0])
            vars.append(list(row)[1])
        if vars[0] > vars[1]:
            print(titles[0], vars[0])
        else:
            print(titles[1], vars[1])
def compare_by_box_office(Title2,Title1):
    column=BoxOffice
    vars = []
    titles = []
    c.execute("SELECT Title, " + column + " FROM movies_generated  WHERE Title='" + Title2 + "' OR Title='" + Title1 + "'")
    vars = []
    titles = []
    earned = 0
    for row in c:
        Title = list(row)[0]
        Money = list(row)[1]
        print(Money)
        if (Money != 'N/A' and Money != None):
            earned = re.findall(r'(\d+.?\d\d+.?\d *\d+.?\d *) *', Money)
            if (len(Money) != 0):
                earned = int(earned[0].replace(',', ''))
        else:
            earned = 0
        print(Money)
        titles.append(list(row)[0])
        vars.append(earned)
    if vars[0] > vars[1]:
        print(titles[0], vars[0])
    else:
        print(titles[1], vars[1])
#####
def compare_by_number_of_awards(Title1,Title2):
    titles=[]
    vars=[]
    column = 'Awards'
    with conn:
        titles = []
        vars = []
        c.execute(
            "SELECT Title, " + column + " FROM movies_generated  WHERE Title='" + Title2 + "' OR Title='" + Title1 + "'")
        for row in c:
            print(row)
            Title = list(row)[0]
            award = list(row)[1]
            # print(award)
            win1 = re.findall(r'(\d+.?\d*) wins', award)
            win2 = re.findall(r'Won (\d+.?\d*)', award)
            if len(win1) == 0:
                win1.append(0)
            if len(win2) == 0:
                win2.append(0)
            all_win = int(win1[0]) + int(win2[0])
            titles.append(Title)
            vars.append(all_win)
        # print(vars)
    if vars[0] > vars[1]:
        print("Won " + str(titles[0]) + " with " + str(vars[0]) + " awards")
    else:
        print("Won " + str(titles[1]) + " with " + str(vars[1]) + " awards")
#class comparing


if __name__ == "__main__":
    ##these lines below are to create table from api
    # whole_data=generate_data_from_api()
    #
    #
    # print(whole_data)
    # whole_data.to_sql(con=conn, name='movies_generated', if_exists='replace')
    # save_to_csv(whole_data)
    #remove_zero_column()

    parser = argparse.ArgumentParser()
    parser.add_argument('--sort_by', type=str,
                        help='type name of column by which you want to sort your table')
    parser.add_argument('--filter_by', type=str,
                        help='type name of column by which you want to sort your table')
    #parser.add_argument('--y', type=float, default=1.0,
                   #     help='What is the second number?')
    #parser.add_argument('--operation', type=str, default='add',
                    #    help='What operation? Can choose add, sub, mul, or div')
    parser.add_argument('--filter_by', nargs='+', help='filtering for specific property of database \n after --filter_by add director or actor to filter database by these categories \n to search for movies that was nominated for oscar but did not win any print "movies_nominated_for_oscar_not_win" \n for movies that won over 80% of nominations print "movies_won_80_percent" \n  for searching movies that earned over 100 000 000 $ print "movies_earned_over_100_000_000"\n to search over movies in certain language write (without quotation marks) two arguments : "language" and after that specific language, for example "English"')
    args = parser.parse_args()
  #  sys.stdout.write(str(sorting(column)))
    if args.sort_by != None:
        sorting(args)
    # elif args[0].filter_by != None:
    #     if (args[0].filter_by=='language'):
    #         lang=args[1].filter_by
    #         movies_in_certain_language(lang)


    # elif args.show != None:
    #     show(args)
    # elif args.delete != None:
    #     delete(args)
    # elif args.copy != None:
    #     copy(args)
    # elif args.rename != None:
    #     rename(args)

    # conn.commit()
    # conn.close()
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





# def print_json(json_data):
#     list_keys=['Title', 'Year', 'Runtime', 'Genre', 'Director', 'Cast', 'Writer', 'Language', 'Country', 'Awards','imbdRating', 'imbdVotes', 'BoxOffice']
#     print("-"*50)
#     for k in list_keys:
#         if k in list(json_data.keys()):
#             print(f"{k}: {json_data[k]}")
#     print("-"*50)
# def add_to_csv(json_data):
#     Csv_keys = ['Title', 'Year', 'Runtime', 'Genre', 'Director', 'Cast', 'Writer', 'Language', 'Country', 'Awards',
#                  'imbdRating', 'imbdVotes', 'BoxOffice']
#     for k in Csv_keys:
#         df['k']


#from omdbapi.movie_search import GetMovie
#omdb.set_default('apikey', ccfc0898)
#movie = GetMovie(title='Interstellar', api_key='ccfc0898')

#from pymatgen.ext.matproj import MPRester

#movie.get_all_data('Year', 'Runtime', 'Genre', 'Director', 'Cast', 'Writer', 'Language', 'Country', 'Awards','imbdRating', 'imbdVotes', 'BoxOffice')

#if __name__ =='__main__':
 #   MAPI_KEY=ccfc0898execute

