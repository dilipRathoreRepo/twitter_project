# twitter_project

'Production' is the main branch with all functionalities. This web application allows users to authenticate themselves via twitter login API and user can authorize this app to get/post tweets on their behalf.
It uses Oauth2.0 for authentication (request tokens, authorization verification and access tokens). Once user is authenticated and authorized, they can 
search the tweets, perform sentiments analysis using text processing API and HTML/CSS styles are used to color the tweets based on if the tweet is positive,
negetive or neutral. User's login information is saved in Postgres database along with access tokens. This application uses sessions/cookies along with OAuth 
so that users don't have to login again and again. Main application file is 'app.py' and Flask and psycopg2 are used.
