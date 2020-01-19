from datetime import datetime
import os
import pytz
import requests
import math
from static import key

API_key = key.key
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')

def query_api(city):
    try:
        print(API_URL.format(city,API_key))
        data = requests.get(API_URL.format(city, API_key)).json()
    except Exception as esc:
        print(esc)
        data = None
    return data
