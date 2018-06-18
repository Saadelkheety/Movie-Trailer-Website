from webbrowser import open_new_tab
class Movie():
    def __init__(self, movie_title, poster_image, trailer_youtube,box_art):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.box_art = box_art
    def show_trailer(self):
        open_new_tab(self.trailer_youtube_url)
