import sqlite3
import re
conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
c = conn.cursor()
with conn:
    c.execute("""SELECT (Title, Language) FROM movies_generated WHERE Language=""")
    conn.commit()
    print(c.fetchall())