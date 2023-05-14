from google.cloud import ndb

class Movie(ndb.Model):
    title = ndb.StringProperty()
    director = ndb.StringProperty()
    cast = ndb.StringProperty()
    genre = ndb.StringProperty()
    poster = ndb.StringProperty()