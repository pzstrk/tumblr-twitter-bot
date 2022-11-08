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
    URL = API_BASE + "posts?api_key=" + API_KEY

    meta_response = requests.get(URL + "&limit=1")
    meta_json = meta_response.json()
    photo_total_num = meta_json["response"]["blog"]["total_posts"]

    index = random.randint(0, photo_total_num - 1)
    print("%s/%s" % (index, photo_total_num))
    
    post_response = requests.get(URL + "&limit=1&offset=" + str(index - 1))
    post_json = post_response.json()
    post = post_json["response"]["posts"][0]
    
    return post

def extract_content(post):
    """
    Get photo urls from tumblr post.
    
    If post was posted from share button, you need to extract photo urls like: https://64.media.tumblr.com/.*?.jpg.
    """
    if post['type'] == 'photo':
        photos = post["photos"]
        photo_urls = []
        for photo in photos:
            photo_urls.append(photo["original_size"]["url"])
        return photo_urls
    elif post['type'] == 'video':
        video_url = post['video_url']
        video_id = twitter_client.UploadMediaChunked(
            media=video_url,
            media_category='tweet_video'
        )
        time.sleep(10)
        return video_id
    #else:
    #    media = re.findall(r'https://64.media.tumblr.com/.*?.jpg', post["body"])

def tweet(media):
    twitter_client.PostUpdate(status='', media=media)
    
if __name__ == '__main__':

    post = get_post()
    media = extract_content(post)
    tweet(media)
