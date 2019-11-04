import sqlite3
import re
conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
c = conn.cursor()
List_of_winners = []
earned=0
with conn:
    c.execute("""SELECT BoxOffice, Title FROM movies_generated""")
    for row in c:
        Title = list(row)[1]
        Money=list(row)[0]
        #print(Money)

        Winner="Has earned over 100 000 000 $ and the money is "
        if (Money !='N/A' and Money!=None):
            earned = re.findall(r'(\d+.?\d\d+.?\d *\d+.?\d *) *', Money)
            earned=int(earned[0].replace(',',''))
        print(earned)
        if earned>100000000:
            List_of_winners.append([Title, Winner ,earned])
print(List_of_winners)