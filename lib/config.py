import json
import os

config_dir = os.getcwd()
config_file = open(os.path.join(config_dir, 'config.json'), 'r')
config = json.load(config_file)
