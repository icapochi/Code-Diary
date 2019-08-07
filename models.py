from google.appengine.ext import ndb

class userData(ndb.Model):
    sUsername = ndb.StringProperty(required = True)
    sPassword = ndb.StringProperty(required = True)


class tweetPost(ndb.Model):
    Author = ndb.StringProperty(required = True)
    oAuthor = ndb.KeyProperty(userData)
    TweetType = ndb.IntegerProperty(required = True)
    Caption = ndb.StringProperty()
    Creationtime= ndb.DateTimeProperty()
