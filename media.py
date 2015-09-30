"""
media.py
    define class Movie
        initialize class attributes

    define class methods
        show_poster
        show_trailer
"""
import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, movie_release_date, movie_cast, movie_poster_image, movie_trailer):
        self.title               = movie_title
        self.release_date        = movie_release_date
        self.cast                = movie_cast
        self.storyline           = movie_storyline
        self.poster_image_url    = movie_poster_image
        self.trailer_youtube_url = movie_trailer

    def show_poster(self):
        webbrowser.open(self.poster_image_url)

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
