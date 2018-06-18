import media
import fresh_tomatoes
# create an instance of Escpae plan 2 movie
ESCAPE = media.Movie("Escape Plan 2: Hades",
                     "https://m.media-amazon.com/images/M/MV5BMTk4NjA0MjUyMF5BMl5BanBnXkFtZTgwMTEzNDQ1NTM@._V1_SY1000_CR0,0,666,1000_AL_.jpg",  # a url for the poster image
                     "https://youtu.be/6Q7vVt-MeXk",
                     "2018 Action 1h 34m")
# create an instance of Ant-Man movie
ANT_MAN = media.Movie("Ant-Man and the Wasp",
                      "https://m.media-amazon.com/images/M/MV5BYjcyYTk0N2YtMzc4ZC00Y2E0LWFkNDgtNjE1MzZmMGE1YjY1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # a url for the poster image
                      "https://youtu.be/8_rTIAOohas",
                      "2018 Fantasy/Science fiction film 2h 5m")
# create an instance of Avengers: Infinity War movie
INFINITY_WAR = media.Movie("Avengers: Infinity War",
                           "https://m.media-amazon.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # a url for the poster image
                           "https://youtu.be/6ZfuNTqbHE8",
                           "2018 Fantasy/Science fiction film 2h 40m")

DEADPOOL_2 = media.Movie("Deadpool 2",
                         "https://m.media-amazon.com/images/M/MV5BMjI3Njg3MzAxNF5BMl5BanBnXkFtZTgwNjI2OTY0NTM@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                         "https://youtu.be/wLeGWcVeIZ4",
                         " 2018 Fantasy/Science fiction film 2 hours")

THOR_R = media.Movie("Thor: Ragnarok",
          "https://m.media-amazon.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
          "https://youtu.be/ue80QwXMRHg",
          "2017 Fantasy/Science fiction film 2h 10m")
# create the list to pass it to the open_movies_page method
movies = [ESCAPE, ANT_MAN, INFINITY_WAR, DEADPOOL_2, THOR_R]
# create the html file and open it
fresh_tomatoes.open_movies_page(movies)
