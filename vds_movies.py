"""
vds_movies.py
    This Python script controls the display of a web site of favorite movies
    based on the specifications for Udacity Full Stack Web Developer
    Nanodegree Project 1, P1:Movie Trailer Website.
"""
import media
import vds_fresh_tomatoes

# define 'favorite' movie based on provided template
#   template has been customized to include movie release date and
#   principal actors
princess_bride = media.Movie(
    "Princess Bride",
    "A love story",
    "1987 (USA)",
    "Cary Elwes, Robin Wright, Mandy Patinkin",
    "http://t3.gstatic.com/images?q="
    "tbn:ANd9GcTbq9_n-cBBM8GKulH_Ld9GghuXTxs6DIXBCD1NlWfVVlwUflH8",
    "https://youtu.be/OfcILoREum8"
    )

rocky = media.Movie(
    "Rocky",
    "A love story of a different type",
    "1976 (USA)",
    "Sylvester Stallone, Carl Weathers, Talia Shire",
    "http://www.gstatic.com/tv/thumb/movieposters/5214/p5214_p_v7_aa.jpg",
    "https://youtu.be/Wif1EzGQ9Fk"
    )

star_wars = media.Movie(
    "Star Wars",
    "A long time ago in a galaxy far, far away...",
    "1977 (USA)",
    "Harrison Ford, Mark Hamill, Carrie Fisher",
    "http://t3.gstatic.com/images?q="
    "tbn:ANd9GcTqRzbG-zvWPx5khd-1D9st1B7FYEq71Gbd2UdaPnrWPwVvY2PX",
    "https://youtu.be/H38MpZtujJc"
    )

for_a_few_dollars_more = media.Movie(
    "For a Few Dollars More",
    "A story about the old West",
    "1965 (USA)",
    "Clint Eastwood, Lee Van Cleef",
    "https://upload.wikimedia.org/wikipedia/"
    "en/a/ad/Forafewdollarsmore.jpg",
    "https://www.youtube.com/watch?v=DDRNEwFOttw"
    )

planet_of_the_apes = media.Movie(
    "Planet of the Apes",
    "Earth ruled by English speaking Apes",
    "1968 (USA)",
    "Charlton Heston, Roddy McDowall, Kim Hunter",
    "http://www.gstatic.com/tv/thumb/movieposters/551/p551_p_v7_aa.jpg",
    "https://youtu.be/4RiypkZjtIM"
    )

platoon = media.Movie(
    "Platoon",
    "A story about men in combat in Vienam",
    "1986 (USA)",
    "Charlie Sheen, Johnny Depp, Willem Dafoe",
    "http://www.gstatic.com/tv/thumb/movieposters/9665/p9665_p_v7_aa.jpg",
    "https://youtu.be/597g60vwJ9s"
    )

# create an array of defined movies
#   call the api to open and display the movie data
movies = [princess_bride,
          rocky,
          star_wars,
          for_a_few_dollars_more,
          planet_of_the_apes,
          platoon]
vds_fresh_tomatoes.open_movies_page(movies)
