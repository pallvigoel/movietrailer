import webbrowser




class Movie():
    """This class represents the blueprint of a movie"""
   
    def __init__(self, title, story, image, trailer):
         """This method  creates a movie
       :param title: title
       :title: str
       
       :param story: storyline
       :title: str
       
       :param image: poster_image_url
       :title: str
       
       param trailer: trailer_youtube_url
       :title: str
       """
        self.title = title
        self.storyline = story
        self.poster_image_url = image
        self.trailer_youtube_url = trailer
