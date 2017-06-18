import webbrowser 
class Movie():
 """This class provides list of movies"""
 def __init__(self,title,story,image,trailer):
  self.title=title 
  self.storyline=story
  self.poster_image_url=image
  self.trailer_youtube_url=trailer
 def show(self):
  webbrowser.open(self.trailer_youtube_url)
