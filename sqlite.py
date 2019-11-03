import sqlite3
import pandas as pd
from sqlalchemy import create_engine
conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
c=conn.cursor()

c.execute("""CREATE TABLE movies_new (
            Title text,
            Year text,
            Runtime text,
            Genre text,
            Director text,
            Writer text,
            Language text,
            Country text,
            Awards text,
            imdbRating text,
            imdbVotes text,
            BoxOffice text
            )""")
# c.execute("""SELECT * FROM movies_new ORDER BY """)
conn.commit()
conn.close()
# df = pd.read_csv('/home/milo/Desktop/Backend/movies.csv', header = 0)
# print(df)
# engine = create_engine('mysql://root:@localhost/test')
# with engine.connect() as conn, conn.begin():
#     df.to_sql('csv', conn, if_exists='append', index=False)