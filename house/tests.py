from flask import json
import requests

BASE = 'http://127.0.0.1:5000/'

response = requests.post(BASE + 'api/v1/houses/1', json={'latitude': 12.5, 'longitude':3.45, 'family_count':4})

print(response.json())