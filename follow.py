#  -*- coding: utf-8 -*-
# Tweepyライブラリをインポート
import tweepy
import time
import sys
import pprint
import setting
import os
import json
import requests
import feedparser
import ssl
import random
from requests_oauthlib import OAuth1Session

pp = pprint.PrettyPrinter(indent=4)

# Setting for each keys
CK = setting.CK
CS = setting.CS
AT = setting.AT
AS = setting.AS
SN = setting.SN

try:
    # auth setting
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth)
    followers = api.followers_ids(SN)
    friends = api.friends_ids(SN)

except:
    print("auth error")

# 一往復後のインターバル
interval = 1200
file_list = []
def words(api=tweepy.API(auth)):

    words = ['follow',
             'followme',
             'cryptocurrency',
             'bitcoin',
             'ripple',
             'ethereum',
             'news',
             'followme',
             'Autofollow',
             'blockchain',
             'analysis',
             'trading']
    word = str(random.choice(words))
    print(word)
    count = 1000
    return api.search(q=word, count=count)


def speak_with_rss():

    # RSS URL
    rss_lists = ["https://cryptop-media.com/feed/"]

    rss_list = str(random.choice(rss_lists))

    # SSL
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

        try:
            # RSS取得
            feed = feedparser.parse(rss_list)
        except:
            print("feed Error")
        try:
            # RSS title
            print("RSS TITLE", feed.feed.title)
        except:
            print("RSS TITLE ERROR")
        entry_link_list = []
        entry_title_list = []
        # RSS  published link
        for entry in feed.entries:
            # print(len(feed.entries))
            # print(entry.published)
            entry_title_list.append(entry.title)
            entry_link_list.append(entry.link)
        link = str(random.choice(entry_link_list))
        title = str(random.choice(entry_title_list))
        # summary = str(random.choice(entry_summary_list))
        print("title->", title)
        print("link->", link)

    return api.update_status(status="#follow #cryptopmedia #news #blockchain" + " "+ title + " " + link)


def GetName(result):
    return result.user.name


def GetUserId(result):
    return result.user.id


def GetUserInfo(result):
    return result.user._json['screen_name']


def FollowAndlike(search_results, file_list):
    i = 0
    for result in search_results:
        i += 1
        username = GetUserInfo(result)
        user_id = GetUserId(result)  # Get user_id
        print("user_id", i, ": ", user_id)
        user = GetName(result)  # Get name
        print('user', ': ', user)
        tweet = result.text
        print('tweet', ': ', tweet)
        t = result.created_at
        try:
            speak_with_rss()
            print("Tweet Done!")
        except:
            print("Tweet error")
        try:
            api.create_favorite(user_id)
            print(user)
            p("Like Done", BMAG)
        except:
            print("Couldn't like it")
            print("-"*40)
        try:
            api.create_friendship(user_id)
            print("Follow Done")
            print("*"*40)
        except:
            print("Already followed him")
            print("-"*40)
        try:
            api.retweet(user_id)
            print("Retweet Done")
            print("-"*40)
        except:
            print("Retweet Error")
        try:
            unfollow(api, followers, friends)
            print("UnFollow Done", BLUE)
            print("*"*40, BLUE)
        except:
            print("Unfollow Error")
        time.sleep(int(interval))


def unfollow(api, followers, friends):
    f = str(random.choice(friends))
    try:
        if f not in followers:
            api.destroy_friendship(f)
            print("{0} Bye!".format(api.get_user(f).screen_name))
    except Exception as e:
        print("Unfoolow Error")


def main():
    search_results = words()
    FollowAndlike(search_results, file_list)


if __name__ == "__main__":
    for k in range(1000000):
        main()
        print("Loop", k, " Done")
        # loop interval
        time.sleep(600)
