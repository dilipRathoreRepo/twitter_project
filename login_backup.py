import constants
import oauth2
import urllib.parse as urlparse
import json
from user import User

# Consumer is just used to identify the app, it cannot be used to make API requests
consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)

# Client is used for making API requests
client = oauth2.Client(consumer)

# Twitter works very well with Oauth library hence we are directly making API calls
# using client. Otherwise, normally, you would use 'requests' library to make these calls.
response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')

if response.status != 200:
    print("An error occurred getting request token from Twitter!")

# qsl = query string parameter. It is used to parse the content
request_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

print("Go to the following site in your brower:")
print("{}?oauth_token={}".format(constants.AUTHORIZATION_URL, request_token['oauth_token']))

oauth_verifier = input("what is the PIN?")

token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)

client = oauth2.Client(consumer, token)
response, content = client.request(constants.ACCESS_TOKEN_URL, 'POST')

access_token = dict(urlparse.parse_qsl(content.decode('utf-8')))
print(access_token)

# Create an authorized token object and use that to perform twitter API calls on behalf of the user
authorized_token = oauth2.Token(access_token['oauth_token'], access_token['oauth_token_secret'])
authorized_client = oauth2.Client(consumer, authorized_token)

# Make Twitter API calls
response, content = authorized_client.request('https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images', 'GET')
if response.status != 200:
    print('An error occurred while searching!')

print(content.decode('utf-8'))
tweets = json.loads(content.decode('utf-8'))

[print(tweet["text"]) for tweet in tweets["statuses"]]

