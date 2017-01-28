import webbrowser

class Movie():
    """ This class provides a way to store movie related information """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, title, trailer, storyline, poster):
        self.title = title
        self.trailer_youtube_url = trailer
        self.storyline = storyline
        self.poster_image_url = poster
        
    def show_trailer(self):
        webbrowser.open(self.trailer)

    def show_poster(self):
        webbrowser.open(self.poster)
