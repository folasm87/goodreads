import xml.etree.ElementTree as ET
from goodreads import app
from rauth.service import OAuth1Service, OAuth1Session
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, OAuth, session

CONSUMER_KEY = 'Q8edIjlM2xSSEECcTajYEg'
CONSUMER_SECRET = 'kcbBGH6meXAh9BFJVbsjxjZnz2I6zg0kduhpIbRw'

oauth = OAuth()

goodreads = oauth.remote_app('goodreads',
    base_url = 'http://www.goodreads.com/',
    request_token_url='http://www.goodreads.com/oauth/request_token',
    access_token_url='http://www.goodreads.com/oauth/access_token',
    authorize_url='http://www.goodreads.com/oauth/authorize',
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET
)

"""

goodreads = OAuth1Service(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    name='goodreads',
    request_token_url='http://www.goodreads.com/oauth/request_token',
    authorize_url='http://www.goodreads.com/oauth/authorize',
    access_token_url='http://www.goodreads.com/oauth/access_token',
    base_url='http://www.goodreads.com/'
    )
    
"""

@app.route('/oauth-authorized')
@goodreads.authorized_handler
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    session['goodreads_token'] = (
        resp['oauth_token'],
        resp['oauth_token_secret']
    )
    session['goodreads_user'] = resp['screen_name']

    flash('You were signed in as %s' % resp['screen_name'])
    return redirect(next_url)



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return goodreads.authorize(callback=url_for('oauth_authorized',
        next=request.args.get('next') or request.referrer or None)

"""
@app.route('/logout')
def logout():
    #User logout/authentication/session management.
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run() 
"""
