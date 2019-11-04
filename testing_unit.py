
########################testing unit, normal units didn't work
import sqlite3


con = sqlite3.connect(":memory:")
cur = con.cursor()
def sorting(category, table_n):
    #str(table_n), str(category),
    with con:
        #cur.execute('SELECT * FROM tab = :tab ORDER BY cat = :cat ASC', {'tab':table_n, 'cat':category})
        cur.execute('SELECT * FROM {} ORDER BY {} ASC'.format(table_n, category) )
        con.commit()
    for row in cur:
        print(row)
        print(list(row))
cur.executescript("""
           create table sort_test(
               Col1,
               Col2,
               Col3
           );

           insert into sort_test(Col1, Col2, Col3) values ('Wladyslaw','Polska','Zuraw');
                     insert into sort_test(Col1, Col2, Col3) values ('Agnieszka','Angola','Antylopa');
                     insert into sort_test(Col1, Col2, Col3) values ('Marcin','Urugwaj','Pies' );
           """)
sorting('Col2', 'sort_test')
#cur.execute('SELECT * FROM sort_test ORDER BY Col2 ASC')
#cur.execute("""Select * from sort_test""")
# print(cur)
for row in cur:
    print(row)
