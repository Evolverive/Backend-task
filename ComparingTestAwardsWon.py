import sqlite3
import re
conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
c = conn.cursor()
column='Awards'
Title1='Gran Torino'
Title2='Seven Pounds'
with conn:
    titles = []
    vars = []
    c.execute("SELECT Title, " + column + " FROM movies_generated  WHERE Title='" + Title2 + "' OR Title='" + Title1 + "'")
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
    print("Won " +str(titles[0]) + " with " + str(vars[0]) + " awards")
else:
    print("Won " +str(titles[1]) + " with " + str(vars[1]) + " awards")