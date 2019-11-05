import sqlite3
import sys

conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
c = conn.cursor()
cursor = conn.execute('select * from movies_generated')
director="David Lean"
with conn:
    names = list(map(lambda x: x[0], cursor.description))
    print(names)
    c.execute("SELECT * FROM movies_generated  WHERE Director='" + director + "'")
    conn.commit()
    print(c.fetchall())