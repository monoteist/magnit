from flask import json
import requests

BASE = 'http://127.0.0.1:5000/'
# Обновление объекта (Существующих данных дома!)
response = requests.post(BASE + 'api/v1/houses/2', json={'latitude': 13.3, 'longitude':12.33, 'family_count':4})
print(response.json())
# Создание и добавление нового объекта в класса House (Добавление нового дома!)
response = requests.post(BASE + 'api/v1/houses/5', json={'latitude': 13.3, 'longitude':12.33, 'family_count':4})
print(response.json())