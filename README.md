# Tumblr to Twitter

The Python implementing of a bot posting photos from Tumblr to Twitter.

## Requirements

- python3
- pytumblr
- python-twitter
- tumblr oauth information
- Twitter oath information

## Getting started

Configure your APIs in `config.json`.

```json
{
  "tumblr": {
    "url": "your.tumblr.com",
    "consumer_key": "",
	"consumer_secret": "",
	"oauth_token": "",
	"oauth_secret": ""
  },
  "twitter": {
    "consumer_key": "",
    "consumer_secret": "",
    "access_token_key": "",
    "access_token_secret": ""
  }
}
```

Install some python modules.

```sh
pip3 install -r requirements.txt
```

Then, run `python3 post.py`.

## Appendix

Here is an example of cron setting for posting photo each 30 minutes.

```
0,30 * * * * python3 post.py >> application.log 2>&1
```
