from webbrowser import open_new_tab


class Movie():
    """ this class is instaniate a movie thumbnail"""

    def __init__(self, movie_title, poster_image, trailer_youtube, box_art):
        """ this is the constructor of the class to provide the required
        information of the movie whch is the title, the poster image link,
        the youtube trailer link, and the box art of the movie"""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.box_art = box_art

    def show_trailer(self):
        """ this method is to show up the trailer in a new tab"""
        open_new_tab(self.trailer_youtube_url)
