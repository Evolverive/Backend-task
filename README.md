# Backend-task
Destination of this repositorium is making operations on database, which is taking it's information from Omdb API.

1.First of all. The task performed in __"_main_"__is making database file by taking Titles from "movies.csv" file and then downloading every needed columns from API to new csv file ("movies_done.csv"). After downloading, dataframe with needed informations is tranformed to SQLite file, which is helping to perform operation on data.

2.Then there's making CLI in TEST_CLI.py which is using every programmed function to get done required tasks


For User:
Use in terminal in this directory file TEST_CLI.py, which is perfomorming functions defined in TestFunctions.py .
If you write "python TEST_CLI.py", then you get help information,
for example if you write: python TEST_CLI.py filtr_by Director "Olivier Nakache, Éric Toledano"

(CLI has helping commands what user should write)
This repo contains a lot of python files with tests of each function, but essential file with a class functions used by CLI is TestFunctions.py
Commands that you can use in Command Line Interface:
-"sort_by":
Sorting by chosen category

-"filtr_by":
Filtering table and printing it by Director, Actors, Language (write one word at the end of the command
    It can also check which movies was nominated for oscar but didn't win any, the command is : "NotWin". 
    Check which movies won at least 80% of nominations, command "80wins".
    Check which movies earned over 100 000 000$ , command "80wins"
    
-"--add"
    Add new movie to datasource

-"--highscores"
    Show the biggest values in Runtime, Box office earnings, Most awards won,Most nominations, Most Oscars, Highest IMDB Rating


Comparing value in specific category between two titles and showing greather, commands:
compare_imdb "arg1" "arg2"
compare_rating "arg1" "arg2"
compare_awards "arg1" "arg2"
compare_runtime "arg1" "arg2"
Example: python TEST_CLI.py compare_imdb "The Shawshank Redemption" "In Bruges"

