# Tumblr to Twitter

The Python implementing of a bot posting photos from Tumblr to Twitter.

## Requirements

- Python3
- requests
- python-twitter
- Tumblr API Key
- Twitter API Keys

## Getting started

Configure your APIs in `config.json`.

```json
{
  "tumblr": {
    "url": "your.tumblr.com",
    "api_key": ""
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
pip3 install requests
pip3 install python-twitter
```

Then, run `python3 post.py`.

## Appendix

Here is an example of cron setting for posting photo each 30 minutes.

```
0,30 * * * * python3 post.py >> application.log 2>&1
```
