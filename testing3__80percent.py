import sqlite3
import re
conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
c = conn.cursor()
sentence='Nominated for 7 Oscars. Another 19 wins & 32 nominations.'
nomination1 = re.findall(r'(\d+.?\d*) nominations', sentence)
nomination2 = re.findall(r'Nominated for (\d+.?\d*)', sentence)
win1 = re.findall(r'(\d+.?\d*) wins', sentence)
win2 = re.findall(r'Won (\d+.?\d*)', sentence)
List_of_winners=[]
with conn:
    c.execute("""SELECT Awards, Title FROM movies_generated""")
    for row in c:
        Title=list(row)[1]
        print(Title)
        Winner=0
        nomination1 = re.findall(r'(\d+.?\d*) nominations', str(row))
        nomination2 = re.findall(r'Nominated for (\d+.?\d*)', str(row))
        win1 = re.findall(r'(\d+.?\d*) wins', str(row))
        win2 = re.findall(r'Won (\d+.?\d*)', str(row))
        if len(nomination1)==0:
            nomination1.append(0)
        if len(nomination2)==0:
            nomination2.append(0)
        if len(win1)==0:
            win1.append(0)
        if len(win2)==0:
            win2.append(0)
        all_nom=int(nomination1[0])+int(nomination2[0])
        all_win = int(win1[0])+int(win2[0])
        if (all_win+all_nom>0):
            percent=(100*all_win/(all_win+all_nom))
        else:
            percent=0
        if percent>80:
            Winner="has won more than 80% of nominations with percent of"
            List_of_winners.append([Title, Winner, percent])
        #c.execute("INSERT INTO movies_generated(percent) VALUES {}".format())
        print(" nominations : %s,%s , wins : %s, %s" %(nomination1,  nomination2, win1, win2))
        print("nom= %s , wins=%s" % (all_nom, all_win))
    conn.commit()
    print(List_of_winners)
  #  print(c.fetchall())