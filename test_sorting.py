from unittest import TestCase

import sqlite3

class TestSorting(TestCase):
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
