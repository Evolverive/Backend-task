from unittest import TestCase

import sqlite3
import re
from urllib.request import urlopen
import json
import pandas as pd
conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
c = conn.cursor()
def change_space_to_plus(title):
    return title.replace(' ', '+')
class TestFunctions(TestCase):
    def compare_by_imbd_rating(Title2, Title1):
        column = imdbRating
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

    def compare_by_box_office(Title2, Title1):
        column = BoxOffice
        vars = []
        titles = []
        c.execute(
            "SELECT Title, " + column + " FROM movies_generated  WHERE Title='" + Title2 + "' OR Title='" + Title1 + "'")
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
    def compare_by_number_of_awards(Title1, Title2):
        titles = []
        vars = []
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

    # class comparing
    def compare_by_runtime(Title1, Title2):
        column = 'Runtime'
        with conn:
            titles = []
            vars = []
            c.execute(
                "SELECT Title, " + column + " FROM movies_generated  WHERE Title='" + Title2 + "' OR Title='" + Title1 + "'")
            for row in c:

                Title = list(row)[0]
                award = list(row)[1]
                win1 = re.findall(r'(\d+.?\d*) min', award)
                if len(win1) == 0:
                    win1.append(0)
                titles.append(Title)
                vars.append(int(win1[0]))
        # print(vars)
        if int(vars[0]) > int(vars[1]):
            print(str(titles[0]) + " is longer and has " + str(vars[0]) + " min")
        else:
            print(str(titles[1]) + " is longer and has " + str(vars[1]) + " min")

    def sorting(category):

        table_n = 'movies_generated'
        with conn:
            # cur.execute('SELECT * FROM tab = :tab ORDER BY cat = :cat ASC', {'tab':table_n, 'cat':category})

            c.execute("SELECT * FROM '"+table_n+"' ORDER BY "+category+" ASC")
            print(category)

        for row in c:
            print(row)
        conn.commit()
    def filtering_director(director):
        conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
        c = conn.cursor()
        cursor = conn.execute('select * from movies_generated')
        with conn:
            names = list(map(lambda x: x[0], cursor.description))
            print(names)
            c.execute("SELECT * FROM movies_generated  WHERE Director='" + director + "'")
            conn.commit()
            print(c.fetchall())
    def filtering_actor(actor):
        conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
        c = conn.cursor()
        cursor = conn.execute('select * from movies_generated')
        with conn:
            names = list(map(lambda x: x[0], cursor.description))
            print(names)
            c.execute("SELECT * FROM movies_generated  WHERE Actors='" + actor + "'")
            conn.commit()
            print(c.fetchall())
    def movies_nominated_for_oscar_not_win():
        conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
        c = conn.cursor()
        with conn:
            c.execute("""SELECT Title FROM movies_generated WHERE (Awards LIKE "Nominated for%"  AND Awards LIKE "%Oscar%" )""")
            conn.commit()
            print(c.fetchall())


    def movies_that_won_over_80_percent():
        conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
        c = conn.cursor()
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
        conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
        c = conn.cursor()
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
                    earned=dolars_to_int(Money)
                print(earned)
                if earned > 100000000:
                    List_of_winners.append([Title, Winner, earned])
        print(List_of_winners)

    def movies_in_certain_language(lang):
        conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
        c = conn.cursor()
        with conn:
            c.execute("SELECT (Title, Language) FROM movies_generated WHERE Language="+lang+")")
            conn.commit()
            print(c.fetchall())
    def add_movie_to_datasource(title):
        serviceurl = 'http://www.omdbapi.com/?t='
        apikey = '&apikey=' + 'ccfc0898'
        url = serviceurl + change_space_to_plus(title) + apikey
        response = urlopen(url)
        data = json.loads(response.read())
        # print(data)
        data_from_api = pd.DataFrame(data=data)
        # print(data_from_api)

        # for column in columns_in_csv:
        clear_data = data_from_api.filter(['Title', 'Year', 'Runtime', 'Genre', 'Director', 'Actors', 'Writer', 'Language', 'Country', 'Awards','imdbRating', 'imdbVotes', 'BoxOffice'], axis=1)
        clear_data = clear_data.iloc[0]
        command = "INSERT INTO movies_generated  ('Title', 'Year', 'Runtime', 'Genre', 'Director', 'Actors', 'Writer', 'Language', 'Country', 'Awards', 'imdbRating', 'imdbVotes', 'BoxOffice' ) VALUES ('"
        for x in range(0,len(clear_data)-1):
            command = command + clear_data[x] + "', '"
        command = command + clear_data[12] + "')"
        c.execute(command)
        #c.execute("INSERT INTO movies_generated ('Title', 'Year', 'Runtime', 'Genre', 'Director', 'Actors', 'Writer', 'Language', 'Country', 'Awards', 'imdbRating', 'imdbVotes', 'BoxOffice' ) VALUES ( '"+clear_data[0]+"', '"+clear_data[1]+"', '"+clear_data[2]+"', '"+clear_data[3]+"', '"+clear_data[4]+"', '"+clear_data[5]+"', '"+clear_data[6]+"', '"+clear_data[7]+"', '"+clear_data[8]+"', '"+clear_data[9]+"', '"+clear_data[10]+"', '"+clear_data[11]+"', '"+clear_data[12]+"'")
        conn.commit()
    def highscores():
        conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
        c = conn.cursor()
        with conn:
            titles = []
            vars = []
            c.execute("SELECT RUNTIME, Title FROM movies_generated ")
            for row in c:
                Title = list(row)[1]
                runtime = list(row)[0]
                runtime_new = re.findall(r'(\d+.?\d*) min', runtime)
                if len(runtime_new) == 0:
                    runtime_new.append(0)
                titles.append(Title)

                vars.append(int(runtime_new[0]))
            maxim = max(vars)
            # print(maxim)
            index = vars.index(maxim)
            print("It is the longest movie")
            print(titles[index], maxim)

        with conn:
            titles = []
            vars = []
            earned = 0
            c.execute("SELECT BoxOffice, Title FROM movies_generated ")
            for row in c:
                Title = list(row)[1]
                Money = list(row)[0]
                if (Money != 'N/A' and Money != None):
                    earned = re.findall(r'(\d+.?\d\d+.?\d *\d+.?\d *) *', Money)
                    earned = int(earned[0].replace(',', ''))
                titles.append(Title)
                vars.append(int(earned))
            # print(vars)
            maxim = max(vars)
            # print(maxim)
            index = vars.index(maxim)
            print("It is the movie with the biggest earnings")
            print(titles[index], maxim)
            # runtime_minutes = re.findall(r'(\d+.?\d*) min', award)
            conn.commit()

            #### THE MOST AWARDS
        with conn:
            titles = []
            vars = []
            earned = 0
            c.execute("SELECT Awards, Title FROM movies_generated ")
            for row in c:
                Title = list(row)[1]
                win1 = re.findall(r'(\d+.?\d*) wins', str(row[0]))
                win2 = re.findall(r'Won (\d+.?\d*)', str(row[0]))
                if len(win1) == 0:
                    win1.append(0)
                if len(win2) == 0:
                    win2.append(0)
                all_win = int(win1[0]) + int(win2[0])
                titles.append(Title)
                vars.append(int(all_win))
            # print(vars)
            maxim = max(vars)
            # print(maxim)
            index = vars.index(maxim)
            print("It is the movie with the most awards")
            print(titles[index], maxim)
            # runtime_minutes = re.findall(r'(\d+.?\d*) min', award)

        with conn:
            titles = []
            vars = []
            earned = 0
            c.execute("SELECT Awards, Title FROM movies_generated ")
            for row in c:
                Title = list(row)[1]
                nomination1 = re.findall(r'(\d+.?\d*) nominations', str(row[0]))
                nomination2 = re.findall(r'Nominated for (\d+.?\d*)', str(row[0]))
                if len(nomination1) == 0:
                    nomination1.append(0)
                if len(nomination2) == 0:
                    nomination2.append(0)
                all_nom = int(nomination1[0]) + int(nomination2[0])
                titles.append(Title)
                vars.append(int(all_nom))
            # print(vars)
            maxim = max(vars)
            # print(maxim)
            index = vars.index(maxim)
            print("It is the movie with the most nominations")
            print(titles[index], maxim)
        with conn:
            titles = []
            vars = []
            earned = 0
            c.execute("SELECT Awards, Title FROM movies_generated ")
            for row in c:
                # print(row)
                Title = list(row)[1]
                oscars = re.findall(r'Won (\d+.?\d*) Oscar', str(row[0]))
                # print(oscars)
                if len(oscars) == 0:
                    oscars.append(0)
                # print(oscars)
                titles.append(Title)
                vars.append(int(oscars[0]))
            maxim = max(vars)
            # print(maxim)
            index = vars.index(maxim)
            print("It is the movie with the most oscars")
            print(titles[index], maxim)
        import sys
        with conn:
            titles = []
            vars = []
            earned = 0
            c.execute("SELECT imdbRating, Title FROM movies_generated ")
            for row in c:
                # print(row)
                Title = list(row)[1]
                rating = list(row)[0]
                # if Title=='The Shawshank Redemption':
                #     print(rating)
                # print(oscars)
                if len(rating) == 0:
                    rating.append(0)
                # print(oscars)
                titles.append(Title)
                # print(list(row)[0])
                vars.append(list(row)[0])

            maxim = max(vars)
           # print(maxim)
            # print(maxim)
            index = vars.index(maxim)
            print("It is the movie with the best imdb_rating")
            print(titles[index], vars[index])