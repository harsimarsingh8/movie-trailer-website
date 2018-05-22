import webbrowser


"""fresh_tomatoes is  module which  has a function"""
"""called open_movies_page that """
"""takes in one argument, which is a list of movies"""
"""here import means that we want to tell python that we want to use webbrowser"""  # noqa
"""and its functionality in our program."""


class Movie():
    """
     This class is storing all the movie related information,
     that we want to see.
     we defined __init__ fn with means its a special function reserved
     by the python to the programmers.
     it creates space for the instances and take keyword [ self ]
     which helps in creating a instance.
     Here self will refer to the new movie object created
     in the entertainment_center.py file.
     """
    valid_ratings = ["A", "U", "UA", "R"]
    # self is pointing to that object only for eg if 22 jump street object is created then self mean 22 jump street.   # noqa

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 movie_poster_teaser,
                 movie_trailer_youtube_url):
        # initialize instance of class Movie
        self.title = movie_title
        # self.title stores the title of the movie
        self.storyline = movie_storyline
        # self.storyline stores the storyline of the movie
        self.poster_image_url = movie_poster_teaser
        # self.poster stores the poster of the movie
        self.trailer_youtube_url = movie_trailer_youtube_url
        # self.trailer stores the trailer of the movie
        # now we make a show_trailer function

    def show_trailer(self):
        # link is stored in a instance variable so we use a self
        webbrowser.open(self.trailer_youtube_url)
