from google.appengine.ext import ndb


class Info(ndb.Model):
    'to describe a book class'
    First = ndb.StringProperty(required=True)
    Email = ndb.StringProperty()
    City = ndb.StringProperty()
    State= ndb.StringProperty()
    Zip   = ndb.StringProperty()
    


