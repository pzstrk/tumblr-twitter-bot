#-*- coding: utf-8 -*-

import json
import random
import re
import os

import twitter
import pytumblr

config_dir = ''
config_file = open(os.path.join(config_dir, 'config.json'), 'r')
config = json.load(config_file)

tumblr_client = pytumblr.TumblrRestClient(
    config['tumblr']['consumer_key'],
    config['tumblr']['consumer_secret'],
    config['tumblr']['oauth_token'],
    config['tumblr']['oauth_secret']
)

twitter_client = twitter.Api(
    consumer_key = config["twitter"]["consumer_key"],
    consumer_secret = config["twitter"]["consumer_secret"],
    access_token_key = config["twitter"]["access_token_key"],
    access_token_secret = config["twitter"]["access_token_secret"],
)

def get_post_from_tumblr(client):
    blog = config['tumblr']['url']
    blog_info = client.blog_info(blog)
    total_num = blog_info['blog']['posts']

    index = random.randint(0, total_num - 1)
    response = client.posts(blog, limit=1, offset=index-1)

    return response['posts'][0]

def extract_content(client, post):
    if post['type'] == 'photo':
        photos = post["photos"]
        photo_urls = []
        for photo in photos:
            photo_urls.append(photo["original_size"]["url"])
        return photo_urls
    elif post['type'] == 'video':
        video_url = post['video_url']
        video_id = client.UploadMediaChunked(
            media=video_url,
            media_category='tweet_video'
        )
        time.sleep(10)
        return video_id
    #else:
    #    media = re.findall(r'https://64.media.tumblr.com/.*?.jpg', post["body"])

def post_tweet(client, media):
    client.PostUpdate(status='', media=media)
    
if __name__ == '__main__':
    post = get_post_from_tumblr(tumblr_client)
    media = extract_content(twitter_client, post)
    post_tweet(twitter_client, media)

