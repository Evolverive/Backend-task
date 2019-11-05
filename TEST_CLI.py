usage = '''

Sorter and Filter CLI.

Usage:
  TEST_CLI.py sort_by [<sort_category>]
  TEST_CLI.py filtr_by [<filter_category>] [<object>]
  TEST_CLI.py --add [<name>]
  TEST_CLI.py --highscores
'''

from docopt import docopt
import os
import test_sorting

print("Program for sorting and filtering.\nHelp:\nTo sort database use: sort_by <sort_category>")
print("To get filtered results use: filtr_by <filter_category> <object>")
print("To add a new movie to the database use: --add <name>")
print("To get highscores use: --highscores")
print("Sort categories: Title, Year, Runtime, Genre, Director, Writer, Language, Country, Awards, imdbRating, imdbVoice, BoxOffice")
print("Filter categories: Director, Actor, Language, NotWin, 80wins, Rich")
print("BoxOffice - box office earnings")
print("NotWin - movies that was nominated  for Oscar but did not win any\n80wins - movies that won more than 80% of nominations")
print("Rich - movies that earned more than 100,000,000 $")
print("Example: __main__.py filtr_by Director Eastwood\n\n")

args = docopt(usage)

if args['sort_by']:
    if os.sys.platform.startswith('linux'):
        os.system('clear')
    elif os.sys.platform.startswith('win32'):
        os.system('cls')
    
    if args['<sort_category>'] :
        category = args['<sort_category>']
        test_sorting.TestSorting.sorting(category)
    else : print("Something gone wrong, look at example: TEST_CLI.py sort_by Title\n")
if args['filtr_by']:
    if os.sys.platform.startswith('linux') : os.system('clear')
    elif os.sys.platform.startswith('win32') : os.system('cls')
    category = args['<filter_category>']
    object = args['<object>']
    if category == "Director" : filtering_director(object)
    elif category == "Actor" : filtering_actor(object)
    elif category == "Language" : movies_in_certain_language(object)
    elif category == "NotWin" : movies_nominated_for_oscar_not_win()
    elif category == "80wins" : movies_that_won_over_80_percent()
    elif category == "Rich" : movies_earned_over_100_000_000()
    else : print("Something gone wrong, look at example: TEST_CLI.py filtr_by Director Eastwood\n")
if args['--add']:
    if os.sys.platform.startswith('linux') : os.system('clear')
    elif os.sys.platform.startswith('win32') : os.system('cls')
    if args['<name>']:
        name = args['<name>']
        add_movie_to_datasource(name)
    else : print("Something gone wrong, look at example: TEST_CLI.py --add \"Pirates of Caribean\"")
if args['--highscores']:
    if os.sys.platform.startswith('linux') : os.system('clear')
    elif os.sys.platform.startswith('win32') : os.system('cls')
    highscores()