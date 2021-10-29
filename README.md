# Tumblr to Twitter

## Requirements

- Python
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
