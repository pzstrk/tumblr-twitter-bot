#-*- coding: utf-8 -*-

import re
import time
import datetime

from lib.config import config
import lib.tumblr as tumblr
import lib.twitter as twitter

def extract_content(post):
    if post['type'] == 'photo':
        photos = post["photos"]
        photo_urls = []
        for photo in photos:
            photo_urls.append(photo["original_size"]["url"])
        return photo_urls
#    elif post['type'] == 'video':
#        video_url = post['video_url']
#        video_id = client.UploadMediaChunked(
#            media=video_url,
#            media_category='tweet_video'
#        )
#        time.sleep(10)
#        return video_id

def log(message, level = 'INFO'):
    timezone = datetime.timedelta(hours=9)
    current_time = datetime.datetime.now(datetime.timezone(timezone))
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    print(f'[{formatted_time}] [{level}] {message}')

if __name__ == '__main__':
    post = tumblr.fetch_one()
    media = extract_content(post)
    try:
        twitter.post(media)
        log(f"{post['id']} successfully posted")
    except Exception as e:
        log(f"{post['id']} post failed: {e}", 'ERROR')
