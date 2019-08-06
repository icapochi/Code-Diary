from models import userData, tweetPost

def seed_data():
    Youssoupha_key = userData( sUsername=" Youssoupha", sPassword = "12345").put()
    E_key = userData( sUsername=" Ibrahima", sPassword = "12345").put()
    Astou_key = userData( sUsername="Astou", sPassword = "12345").put()
    Zaina_key = userData( sUsername="Zaina", sPassword = "12345").put()

    tweetPost1= tweetPost(Author="Youssoupha", TweetType= 1, Caption= "I like turtles.").put()
    tweetPost2= tweetPost(Author="Ibrahima", TweetType= 1, Caption= "E is my name.").put()
    tweetPost1= tweetPost(Author="Astou", TweetType= 1, Caption= "Trump isnt that bad.").put()
    tweetPost1= tweetPost(Author="Zaina", TweetType= 1, Caption= "Im only 14.").put()
