import sqlite3
import re
conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
c = conn.cursor()
column='imdbRating'
Title1='Fight Club'
Title2='Goodfellas'
with conn:

    c.execute("SELECT Title, " + column + " FROM movies_generated  WHERE Title='" + Title2 + "' OR Title='" + Title1 +"'")
    #c.execute()
    vars=[]
    titles=[]
    for row in c:
        titles.append(list(row)[0])
        vars.append(list(row)[1])
    if vars[0]>vars[1]:
        print(titles[0],vars[0])
    else:
        print(titles[1],vars[1])

    #c.execute("SELECT Title, (%s) FROM movies_generated WHERE Title=(%s) or Title=(%s)", (column,Title1,Title2))
    #c.execute('SELECT Title, {} FROM movies_generated WHERE Title={} or Title={}'.format(column, Title1, Title2))
   # c.execute("""SELECT Title, imdbRating FROM movies_generated WHERE Title='Goodfellas'""")
    # for row in c:
    #     print(row)
#    c.execute()
    # c.execute("SELECT Title, " + column + "FROM movies_generated WHERE Title="+Title1)
    # for row in c:
    #     print(row)
