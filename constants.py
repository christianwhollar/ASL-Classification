import json

with open('kaggle.json', 'r') as f:
    kaggle_dict = json.load(f)

# kaggle credentials
KAGGLE_USERNAME = kaggle_dict['username']
KAGGLE_API_KEY = kaggle_dict['key']

# robowflow credentials
ROBOFLOW_KEY = ''
ROBOWFLOW_PROJECT = ''
ROBOWFLOW_VERSION = ''