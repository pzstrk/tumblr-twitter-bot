import random

import pytumblr

from lib.config import config

tumblr_client = pytumblr.TumblrRestClient(
    config['tumblr']['consumer_key'],
    config['tumblr']['consumer_secret'],
    config['tumblr']['oauth_token'],
    config['tumblr']['oauth_secret']
)

def fetch_one():
    blog = config['tumblr']['url']
    blog_info = tumblr_client.blog_info(blog)
    total_num = blog_info['blog']['posts']

    index = random.randint(0, total_num - 1)
    response = tumblr_client.posts(blog, limit=1, offset=index-1)

    return response['posts'][0]

