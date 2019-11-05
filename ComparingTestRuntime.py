import sqlite3
import re
conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
c = conn.cursor()
column='Runtime'
Title1='Gran Torino'
Title2='Shazam'
with conn:
    titles = []
    vars = []
    c.execute("SELECT Title, " + column + " FROM movies_generated  WHERE Title='" + Title2 + "' OR Title='" + Title1 + "'")
    for row in c:
        print(row)
        Title = list(row)[0]
        award = list(row)[1]
        print(award)
        print(Title)
        win1 = re.findall(r'(\d+.?\d*) min', award)
        print(win1[0])
        if len(win1) == 0:
            win1.append(0)
        titles.append(Title)
        vars.append(int(win1[0]))
print(vars[0])
print(type(vars[0]))
    # print(vars)
if int(vars[0]) > int(vars[1]):
    print(str(titles[0]) + " is longer and has " + str(vars[0]) + " min")
else:
    print(str(titles[1]) + " is longer and has " + str(vars[1]) + " min")