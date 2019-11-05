import sqlite3
import re
conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
c = conn.cursor()
column = 'Runtime'
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
    maxim=max(vars)
    #print(maxim)
    index=vars.index(maxim)
    print("It is the longest movie")
    print(titles[index] ,maxim )

with conn:
    titles = []
    vars = []
    earned=0
    c.execute("SELECT BoxOffice, Title FROM movies_generated ")
    for row in c:
        Title = list(row)[1]
        Money = list(row)[0]
        if (Money != 'N/A' and Money != None):
            earned = re.findall(r'(\d+.?\d\d+.?\d *\d+.?\d *) *', Money)
            earned = int(earned[0].replace(',', ''))
        titles.append(Title)
        vars.append(int(earned))
    #print(vars)
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
    earned=0
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
    earned=0
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
    #print(vars)
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
        #print(row)
        Title = list(row)[1]
        oscars = re.findall(r'Won (\d+.?\d*) Oscar', str(row[0]))
        #print(oscars)
        if len(oscars) == 0:
            oscars.append(0)
        #print(oscars)
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
        #print(row)
        Title = list(row)[1]
        rating = list(row)[0]
        # if Title=='The Shawshank Redemption':
        #     print(rating)
        #print(oscars)
        if len(rating) == 0:
            rating.append(0)
        #print(oscars)
        titles.append(Title)
        #print(list(row)[0])
        vars.append(list(row)[0])

    maxim = max(vars)
    print(maxim)
    # print(maxim)
    index = vars.index(maxim)
    print("It is the movie with the best imdb_rating")
    print(titles[index], vars[index])
