from google.appengine.ext import ndb

class userData(ndb.Model):
    sUsername = ndb.StringProperty(required = True)
    sPassword = ndb.StringProperty(required = True)
    sAge = ndb.IntegerProperty(required = True)

class tweetPost(ndb.Model):
    Author = nbd.StringProperty(required = True)
    TweetType = nbd.IntegerProperty(required = True)
    Caption = nbd.StringProperty()
    
