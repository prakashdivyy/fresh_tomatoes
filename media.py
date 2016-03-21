import webbrowser

class Movie:
    """ Class Movie

    Attributes:
        title (str): Movie's title
        storyline (str): Movie's storyline
        poster_image_url (str): Movie's poster image URL
        trailer_youtube_url (str): Movie's trailer YouTube URL
        
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Open Web Browser and show movie's trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
