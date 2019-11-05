from unittest import TestCase

import sqlite3

class TestFunctions(TestCase):
   
    def sorting(category):
        conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
        c = conn.cursor()
        table_n = 'movies_generated'
        with conn:
            # cur.execute('SELECT * FROM tab = :tab ORDER BY cat = :cat ASC', {'tab':table_n, 'cat':category})

            c.execute("SELECT * FROM '"+table_n+"' ORDER BY "+category+" ASC")
            print(category)

        for row in c:
            print(row)
        conn.commit()
    def filtering_director(director):
        director=str(director)
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
            c.execute("SELECT Title, Language FROM movies_generated WHERE Language='"+lang+"'")
            conn.commit()
            print(c.fetchall())