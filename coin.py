# -*- coding: utf-8 -*-
# Tweepyライブラリをインポート
import tweepy
import time
import sys
import pprint
import setting
import os
import json
import requests
import random
from requests_oauthlib import OAuth1Session

pp = pprint.PrettyPrinter(indent=4)

coins = [
            [1,  'BTC',  'btc_jpy'],
            [2,  'XEM',  'xem_jpy'],
            [3,  'MONA', 'mona_jpy'],
        ]
zaifbase = 'https://api.zaif.jp/api/1/last_price/'

def coin():
    for i in range(len(coins)):
        response = requests.get(zaifbase+coins[i][2])
        if response.status_code != 200:
            raise Exception('return status code is {}'.format(response.status_code))
        
        rate = json.loads(response.text)
        print(api.update_status(status="%-4s : \%-10s" % (coins[i][1], rate['last_price'])))
