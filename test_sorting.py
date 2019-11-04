from unittest import TestCase

import sqlite3

class TestSorting(TestCase):
    def test_sorting(self):
        # conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
        # cur = conn.cursor()
        # cur.executescript(''' DROP TABLE [IF EXISTS] sort_test;
        #                 CREATE TABLE sort_test (Col1 , Col2 , Col3 );
        #              insert into sort_test(Col1, Col2, Col3) values ('Wladyslaw','Polska','Zuraw');
        #              insert into sort_test(Col1, Col2, Col3) values ('Agnieszka','Angola','Antylopa');
        #              insert into sort_test(Col1, Col2, Col3) values ('Marcin','Urugwaj','Pies' );
        #              ''')
        import mov
        con = sqlite3.connect(":memory:")
        cur = con.cursor()
        cur.executescript("""
            create table person(
                firstname,
                lastname,
                age
            );

            create table book(
                title,
                author,
                published
            );

            insert into book(title, author, published)
            values (
                'Dirk Gently''s Holistic Detective Agency',
                'Douglas Adams',
                1987
            );
            """)
        con.commit()
        assert mov.sorting(Col1, sort_test)
        print(cur.fetchall())
        cur.close()

        self.fail()
