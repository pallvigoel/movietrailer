import webbrowser


class Movie():
    """This class represents the blueprint of a movie"""

    def __init__(self, title, story, image, trailer):
        """This method  creates a movie

        :param title: title
        :type title: str

        :param story: storyline
        :type story: str

        :param image: poster_image_url
        :type image: str

        param trailer: trailer_youtube_url
        :type trailer: str
        """
        self.title = title
        self.storyline = story
        self.poster_image_url = image
        self.trailer_youtube_url = trailer
