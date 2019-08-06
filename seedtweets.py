#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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

seed_data()
