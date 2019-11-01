import constants
import oauth2
import urllib.parse as urlparse
from user import User
from database import Database
from twitter_utils import consumer

email = 'rathore.gecg@gmail.com'
URI = 'https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images'
VERB = 'GET'

client = oauth2.Client(consumer)

Database.initialise(user='postgres', password='admin', database='learning', host='localhost')
user = User.load_from_db_by_email(email)

if not user:
    print("Entry does not exist.. creating a record in users table")

    response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')

    if response.status != 200:
        print("An error occurred getting request token from Twitter!")

    request_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

    print("Go to the following site in your browser:")
    print("{}?oauth_token={}".format(constants.AUTHORIZATION_URL, request_token['oauth_token']))

    oauth_verifier = input("what is the PIN?")

    token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
    token.set_verifier(oauth_verifier)

    client = oauth2.Client(consumer, token)
    response, content = client.request(constants.ACCESS_TOKEN_URL, 'POST')

    access_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

    first_name = input("Enter user first name")
    last_name = input("Enter user last name")
    user = User(email, first_name, last_name, None, access_token['oauth_token'], access_token['oauth_token_secret'])
    user.save_to_db()

content = user.twitter_request(URI)
tweets = content

[print(tweet["text"]) for tweet in tweets["statuses"]]
