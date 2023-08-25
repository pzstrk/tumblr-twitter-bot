import tweepy

from lib.config import config

CONSUMER_KEY = config["twitter"]["consumer_key"]
CONSUMER_SECRET = config["twitter"]["consumer_secret"]
ACCESS_TOKEN_KEY = config["twitter"]["access_token_key"]
ACCESS_TOKEN_SECRET = config["twitter"]["access_token_secret"]

twitter_v2 = tweepy.Client(
    consumer_key = CONSUMER_KEY,
    consumer_secret = CONSUMER_SECRET,
    access_token = ACCESS_TOKEN_KEY,
    access_token_secret = ACCESS_TOKEN_SECRET
)

def post(text):
    twitter_v2.create_tweet(text=text)

