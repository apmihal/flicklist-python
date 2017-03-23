import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movieList = [
        "Fargo",
        "The Big Lebowski",
        "Star Wars: A New Hope",
        "UHF",
        "2001: A Space Oddyssey"
        ]

        # TODO: randomly choose one of the movies, and return it
        return movieList[random.randrange(0, len(movieList))]

        #return "The Big Lebowski"

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        secondMovie = self.getRandomMovie()
        while secondMovie == movie:
            secondMovie = self.getRandomMovie()

        content += "<h1>Tommorrow's Movie</h1>"
        content += "<p>" + secondMovie + "</p>"

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
