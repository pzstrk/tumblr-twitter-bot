import os
import requests

import tweepy

from lib.config import config

CONSUMER_KEY = config["twitter"]["consumer_key"]
CONSUMER_SECRET = config["twitter"]["consumer_secret"]
ACCESS_TOKEN_KEY = config["twitter"]["access_token_key"]
ACCESS_TOKEN_SECRET = config["twitter"]["access_token_secret"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

twitter_v1 = tweepy.API(auth)

twitter_v2 = tweepy.Client(
    consumer_key = CONSUMER_KEY,
    consumer_secret = CONSUMER_SECRET,
    access_token = ACCESS_TOKEN_KEY,
    access_token_secret = ACCESS_TOKEN_SECRET
)

def upload(url):
    fname = os.path.basename(url)
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(fname, 'wb') as image:
            for chunk in request:
                image.write(chunk)
        media = twitter_v1.media_upload(fname)
        os.remove(fname)
        return(media.media_id)
    else:
        printe("Unable to download image")

def post(text, media_id):
    twitter_v2.create_tweet(text=text, media_ids=[media_id])

