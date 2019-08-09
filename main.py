#main.py
# the import section
import webapp2
import jinja2
import os
import datetime
from google.appengine.ext import ndb
from models import userData, tweetPost
from google.appengine.api import users
from seedtweets import seed_data
import time


# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# the handler section
class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        result_template = the_jinja_env.get_template('templates/result.html')
        self.response.write(result_template.render())  # the response


class results(webapp2.RequestHandler):
    def get(self):  # for a get request
        user = users.get_current_user()
        if user:
            email = user.email()
            email_address = user.nickname()
            login_url = users.create_logout_url('/result')
            tweet_info = tweetPost.query().order(-tweetPost.Creationtime).fetch(10)
            result_template = the_jinja_env.get_template('templates/result.html')
            self.response.write(result_template.render({'tweet_info' : tweet_info, "user" : user, "login_url" : login_url}))
        else:
            email = None
            login_url = users.create_login_url('/result')

            tweet_info = tweetPost.query().order(-tweetPost.Creationtime).fetch(10)
            result_template = the_jinja_env.get_template('templates/result.html')
            self.response.write(result_template.render({'tweet_info' : tweet_info, "user" : user, "login_url" : login_url}))
    def post(self):
        # user = users.get_current_user()
        # nickname = user.nickname()
        # Use the user input to create a new blog post
        user = users.get_current_user()
        if user:
            email = user.email()
            login_url = users.create_logout_url('/result')
            name_input = self.request.get('name')
            description_input = self.request.get('description')
            currenttime= datetime.datetime.now()
            tweetoutput = tweetPost(Author=name_input, Caption=description_input, TweetType=1, Creationtime=currenttime)
            tweetoutput.put()
            time.sleep(1)
            tweet_info = tweetPost.query().order(-tweetPost.Creationtime).fetch(10)
            result_template = the_jinja_env.get_template('templates/result.html')
            self.response.write(result_template.render({'tweet_info' : tweet_info, "user" : user, "login_url" : login_url}))

class logged(webapp2.RequestHandler):
    def get(self):
        logged_in_template = the_jinja_env.get_template('templates/signUp.html')
        self.response.write(logged_in_template.render())

class navToSign(webapp2.RequestHandler):
    def get(self):
        signup_template = the_jinja_env.get_template('templates/signUp.html')
        self.response.write(signup_template.render())

class welcome(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())


# the app configuration section
app = webapp2.WSGIApplication([
    #('/', EnterInfoHandler), #this maps the root url to the Main Page Handler
    ('/result', results),
    ('/in', logged),
    ('/signup', navToSign),
    ('/', welcome)
], debug=True)
