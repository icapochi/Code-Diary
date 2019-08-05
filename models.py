from google.appengine.ext import ndb

class userData(ndb.Model):
    sUsername = ndb.StringProperty(required = True)
    sPassword = ndb.StringProperty(required = True)
    sAge = ndb.IntegerProperty(required = True)
