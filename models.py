from google.appengine.ext import ndb

class userData(ndb.Model):
    sEmail = ndb.StringProperty(required = True)
    sUsername = ndb.StringProperty(required = True)
    sPassword = ndb.StringProperty(required = True)
    sLong = ndb.FloatProperty(default = 41.1792)
    sLat = ndb.FloatProperty(default = -73.1894)


class tweetPost(ndb.Model):
    Author = ndb.StringProperty(required = True)
    oAuthor = ndb.KeyProperty(userData)
    TweetType = ndb.IntegerProperty(required = True)
    Caption = ndb.StringProperty()
    Creationtime= ndb.DateTimeProperty()
