import json
import os

config_dir = os.path.dirname(os.path.abspath(__file__))
config_file = open(os.path.join(config_dir, 'config.json'), 'r')
config = json.load(config_file)
