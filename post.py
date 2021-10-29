#-*- coding: utf-8 -*-

import json
import random
import re

import requests
import twitter

config_file = open('config.json', 'r')
config = json.load(config_file)

API_BASE = "https://api.tumblr.com/v2/blog/%s/" % config["tumblr"]["url"]
API_KEY = config["tumblr"]["api_key"]

twitter_client = twitter.Api(
    consumer_key = config["twitter"]["consumer_key"],
    consumer_secret = config["twitter"]["consumer_secret"],
    access_token_key = config["twitter"]["access_token_key"],
    access_token_secret = config["twitter"]["access_token_secret"],
)

def get_post():
    """
    Get a random tumblr post from all photo posts.
    """
    URL = API_BASE + "posts/photo?api_key=" + API_KEY

    meta_response = requests.get(URL + "&limit=1")
    meta_json = meta_response.json()
    photo_total_num = meta_json["response"]["blog"]["total_posts"]

    index = random.randint(0, photo_total_num - 1)
    print("%s/%s" % (index, photo_total_num))
    
    post_response = requests.get(URL + "&limit=1&offset=" + str(index - 1))
    post_json = post_response.json()
    post = post_json["response"]["posts"][0]
    
    return post

def extract_photo_urls(post):
    """
    Get photo urls from tumblr post.
    
    If post was posted from share button, you need to extract photo urls like: https://64.media.tumblr.com/.*?.jpg.
    """
    urls = []
    if "photos" in post:
        photos = post["photos"]
        for photo in photos:
            urls.append(photo["original_size"]["url"])
    else:
        urls = re.findall(r'https://64.media.tumblr.com/.*?.jpg', post["body"])
    
    return urls

def tweet(urls):
    """
    Post tweet via twitter client.
    """
    twitter_client.PostUpdate(status="", media=urls)

if __name__ == '__main__':

    post = get_post()
    urls = extract_photo_urls(post)
    tweet(urls)