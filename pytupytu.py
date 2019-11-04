usage = '''
Usage:
 pytupytu.py sort_by <sort_category>
Options:
  --countdown  display a count down
'''

import docopt
args = docopt.docopt(usage)

def view(category=None):
    return category

if args['sort_by']:
    category = args['sort_category']
    category = view(category)
    if category == "Title":
        print ("Sortowanie po tytule")
    elif category == "Year":
        print ("Sortowanie po roku")
    elif category == "Runtime":
        print ("Sortowanie po czasie trwania")
    elif category == "Genre":
        print ("Sortowanie po gatunku")
    elif category == "Director":
        print ("Sortowanie po rezyserze")
    elif category == "Writer":
        print ("Sortowanie po scenarzyscie")
    elif category == "Language":
        print ("Sortowanie po jezyku")
    elif category == "Country":
        print ("Sortowanie po kraju")
    elif category == "Awards":
        print ("Sortowanie po nagrodach")
    elif category == "imdbRating":
        print ("Sortowanie po jakims rankingu")
    elif category == "imdbVotes":
        print ("Sortowanie po glosach")
    elif category == "BoxOffice":
        print ("Sortowanie po czyms tam")
    