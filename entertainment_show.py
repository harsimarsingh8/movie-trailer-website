import media
import fresh_tomatoes
# using the contents of our previous file.

Grown_ups = media.Movie("Grown Ups",
                        "Five friends reunite for their high-school coach's funeral. ",                         # noqa
                        "./images/ab.jpg",
                        "https://www.youtube.com/watch?v=cjfuK5QJyEQ")

# here media is a module and Movie is a class which creates a movie instances.


fast_and_furious = media.Movie("Fast And Furious",
                               "A spate of high-speed robberies in LA",
                               "./images/7.jpg",
                               "https://www.youtube.com/watch?v=uisBaTkQAEs")


Home_alone = media.Movie("Home Alone",
                         "Eight-year-old Kevin is accidentally left behind when his family leaves for France",   # noqa
                         "./images/4.jpg",
                         "https://www.youtube.com/watch?v=CK2Btk6Ybm0")

We_are_your_friends = media.Movie("We Are Your Friends",
                                  "Cole Carter, an aspiring DJ, gets involved with his mentor's girlfriend"      # noqa
                                  "and puts his career and their friendship at stake.",   # noqa
                                  "./images/3.jpg",
                                  "https://www.youtube.com/watch?v=gZzAeYWXFpk")          # noqa

twenty_one_jump_street = media.Movie("22 Jump Street",
                                     "Schmidt and Jenko, two undercover cops, are sent on a mission"    # noqa
                                     "to a college to investigate the use of a recreational drug known as WHYPHY. ",  # noqa
                                     "./images/5.jpg",
                                     "https://www.youtube.com/watch?v=v9S_dYuq0vE")     # noqa


Titanic = media.Movie("Titanic",
                      " Titanic is an epic, action-packed romance"                      # noqa
                      "set against the ill-fated maiden voyage of the R.M.S. ",         # noqa
                      "./images/6.jpg",
                      "https://www.youtube.com/watch?v=ZQ6klONCq4s")


Van_helsing = media.Movie("Van Helsing",
                          "Van Helsing, a monster hunter, is sent to Transylvania"                 # noqa
                          "in order to prevent Count Dracula from realising his evil motives.",    # noqa
                          "./images/2.jpg",
                          "https://www.youtube.com/watch?v=7pBmXkyycWE")


X_men = media.Movie("X-men",
                    "They are children of the atom, homo superior,"
                    "the next link in the chain of evolution.",
                    "./images/8.png",
                    "https://www.youtube.com/watch?v=kUCUGEWCNmo")

movies_name = [Grown_ups, fast_and_furious, Home_alone, We_are_your_friends, twenty_one_jump_street, Titanic, Van_helsing, X_men]   # noqa
fresh_tomatoes.open_movies_page(movies_name)
# calling list (movies) as an input to open_movies_page.
print (media.Movie.valid_ratings)
# as we all know that media is a module in which movie is a class
# to print module name --->
print (media.Movie.__module__)
