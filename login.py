import oauth2
from twitter_utils import consumer, get_request_token, get_oauth_verifier, get_access_token
from user import User
from database import Database

email = 'rathore.gecg@gmail.com'
URI = 'https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images'
VERB = 'GET'

Database.initialise(user='postgres', password='admin', database='learning', host='localhost')
user = User.load_from_db_by_email(email)

if not user:
    print("Entry does not exist.. creating a record in users table")

    request_token = get_request_token()

    oauth_verifier = get_oauth_verifier(request_token)

    access_token = get_access_token(request_token, oauth_verifier)

    first_name = input("Enter user first name")
    last_name = input("Enter user last name")
    user = User(email, first_name, last_name, None, access_token['oauth_token'], access_token['oauth_token_secret'])
    user.save_to_db()

content = user.twitter_request(URI)
tweets = content

[print(tweet["text"]) for tweet in tweets["statuses"]]
