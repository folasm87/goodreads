from goodreads import app

import facebook
from flask import Flask
from flask import render_template
from rauth.service import OAuth1Service, OAuth1Session
from social.apps.flask_app.routes import social_auth

#app = Flask(__name__)

"""
We're going to use OAuth authorization to retrieve the username. We'll display this as a headline.
Afterwards we retrieve a user's most liked books, authors of said books and match them against facebook pages.
If any corresponding facebook pages are found we create a timeline of sorts. 

"""


CONSUMER_KEY = 'Q8edIjlM2xSSEECcTajYEg'
CONSUMER_SECRET = 'kcbBGH6meXAh9BFJVbsjxjZnz2I6zg0kduhpIbRw'
token = '220175958043754|4Lx4YRnWu4j5vHfLH4n7eZyfluw' #facebook token

graph = facebook.GraphAPI(token)

goodreads = OAuth1Service(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    name='goodreads',
    request_token_url='http://www.goodreads.com/oauth/request_token',
    authorize_url='http://www.goodreads.com/oauth/authorize',
    access_token_url='http://www.goodreads.com/oauth/access_token',
    base_url='http://www.goodreads.com/'
    )

# head_auth=True is important here; this doesn't work with oauth2 for some reason
request_token, request_token_secret = goodreads.get_request_token(header_auth=True)

authorize_url = goodreads.get_authorize_url(request_token)
print 'Visit this URL in your browser: ' + authorize_url
accepted = 'n'
while accepted.lower() == 'n':
    # you need to access the authorize_link via a browser,
    # and proceed to manually authorize the consumer
    accepted = raw_input('Have you authorized me? (y/n) ')


session = goodreads.get_auth_session(request_token, request_token_secret)

# book_id 631932 is "The Greedy Python"
data = {'name': 'to-read', 'book_id': 631932}

# add this to our "to-read" shelf
response = session.post('http://www.goodreads.com/shelf/add_to_shelf.xml', data)

# these values are what you need to save for subsequent access.
ACCEESS_TOKEN = session.access_token
ACCESS_TOKEN_SECRET = session.access_token_secret


"""
Pass authorize_url as an argument to the template
Figure how to autoload a url?

Just have a button on the index that asks you to sign in to your Goodreads account. 

Similar for facebook api


"""

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')




'''
if __name__ == '__main__':
    app.run() 
'''