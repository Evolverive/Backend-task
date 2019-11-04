import sqlite3
import re
conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
c = conn.cursor()
column='Awards'
Title1='Gran Torino'
Title2='Seven Pounds'
with conn:
    vars = []
    titles = []
    c.execute(
        "SELECT Title, " + column + " FROM movies_generated  WHERE Title='" + Title2 + "' OR Title='" + Title1 + "'")
    # c.execute()
    vars = []
    titles = []
    earned=0
    for row in c:
        Title = list(row)[0]
        Money = list(row)[1]
        print(Money)
        if (Money != 'N/A' and Money != None):
            earned = re.findall(r'(\d+.?\d\d+.?\d *\d+.?\d *) *', Money)
            if (len(Money)!=0):
                earned = int(earned[0].replace(',', ''))
        else:
            earned=0
        print(Money)
        titles.append(list(row)[0])
        vars.append(earned)
    if vars[0] > vars[1]:
        print(titles[0], vars[0])
    else:
        print(titles[1], vars[1])