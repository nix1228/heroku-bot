# Dependencies
import tweepy
import json
import time


# Twitter API Keys
consumer_key = "W6o1gtXQvt8JxAmf5DgbQDQRC"
consumer_secret = "nVt0WcFRpMVTbhfQH7n1yyJKCyuc76XvNe3WWoO3K9zelEZnzB"
access_token = "969399075173941249-g9c4zmMcuOLStEc3bVwifJxxC980cFm"
access_token_secret = "XqwynliZFJFT0DPR7mtf9fUzBiVRfCbQqrLbQlpQ8pBTB"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
