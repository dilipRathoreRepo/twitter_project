# import psycopg2
from user import User
from database import Database

Database.initialise(user='postgres', password='admin', database='learning', host='localhost')
try:
    user = User.load_from_db_by_email('XXXX@gmail.com')
    print('oauth_token and oauth_token_secret are : {} and {}'.format(user.oauth_token, user.oauth_token_secret))
except TypeError:
    print("invalid email")
