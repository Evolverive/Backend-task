import testing_unit
import mov
Usage:
  mov.py testing_unit.sorting() [--sort_by] <category>
  mov.py ship <name> move <x> <y> [--speed=<kn>]
  mov.py ship shoot <x> <y>
  mov.py mine (set|remove) <x> <y> [--moored|--drifting]
  mov.py -h | --help
  mov.py --version

from docopt import docopt

def init():
    '''
    Initialize a new database to store the
    expenditures
    '''
    conn = sqlite3.connect('/home/milo/Desktop/Backend/movies.sqlite')
    cur = conn.cursor()
    sql = '''
    create table if not exists expenses (
        amount number,
        category string,
        message string,
        date string
        )
    '''
    cur.execute(sql)
    conn.commit()


args=docopt(usage)
if args['sort_by']:
    mov.sorting(args)
if args['filter_by']:



print args