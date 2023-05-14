import os
import json
import jinja2
import webapp2
import requests
from google.cloud import ndb
from models.movie import Movie

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))


class MainHandler(webapp2.RequestHandler):

    def get(self):
        template = jinja_env.get_template('base.html')
        self.response.write(template.render())

class SearchMoviesHandler(webapp2.RequestHandler):
    
    def get(self):
        template = jinja_env.get_template('movie_search.html')
        self.response.write(template.render())

    def post(self):
        client = ndb.Client()

        search_option = self.request.get('search_option')
        query = self.request.get('search')
        with client.context():
            if search_option == 'director':
                movies = Movie.query(Movie.director == query)
            elif search_option == 'cast':
                movies = Movie.query(Movie.cast == query)
            elif search_option == 'genre':
                movies = Movie.query(Movie.genre == query)
            else:
                movies = []
            template = jinja_env.get_template('movie_list.html')
            self.response.write(template.render(movies=movies))

class ListMoviesHandler(webapp2.RequestHandler):
    
    def get(self):
        client = ndb.Client()
        with client.context():
            movies = Movie.query()
            template = jinja_env.get_template('movie_list.html')
            self.response.write(template.render(movies=movies))

class AddMovieHandler(webapp2.RequestHandler):
    
    def get(self):

        template = jinja_env.get_template('movie_form.html')
        self.response.write(template.render())

    def post(self):

        client = ndb.Client()
        title = self.request.get("title")
        response = requests.get(f"http://www.omdbapi.com/?apikey=<API_KEY>&t={title}")
        data = json.loads(response.text)
        with client.context():
            movie = Movie(title=data["Title"],director=data["Director"],cast=data["Actors"],genre=data["Genre"],poster=data["Poster"])
            movie.put()

        self.redirect("/list")

class EditMovieHandler(webapp2.RequestHandler):
    
    def get(self):
        id = self.request.get('id')
        client = ndb.Client()
        with client.context():
            movie = ndb.Key('Movie', int(id)).get()
            template = jinja_env.get_template('movie_edit.html')
            self.response.write(template.render(movie=movie))
            
    def post(self):
        id = self.request.get('id')
        client = ndb.Client()
        with client.context():
            movie = ndb.Key('Movie', int(id)).get()
            title = self.request.get('title') or movie.title
            director = self.request.get('director') or movie.director
            cast = self.request.get('cast') or movie.cast
            genre = self.request.get('genre') or movie.genre
            poster = self.request.get('poster') or movie.poster
            movie.title = title
            movie.director = director
            movie.cast = cast
            movie.genre = genre
            movie.poster = poster
            movie.put()
        self.redirect('/list')



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/search', SearchMoviesHandler),
    ('/list', ListMoviesHandler),
    ('/add', AddMovieHandler),
    ('/edit', EditMovieHandler),
], debug=True)