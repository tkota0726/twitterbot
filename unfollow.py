# coding: utf-8
import tweepy
import time
import setting

# 各種キーをセット

CK= setting.CK
CS= setting.CS
AT= setting.AT
AS= setting.AS
SN= setting.SN

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

def unfollow(api,followers, friends):
    unfollow_cnt = 0
    for f in friends:
        if f not in followers:
            if unfollow_cnt <= 100:
                api.destroy_friendship(f)
                print(unfollow_cnt, "{0} Bye!".format(api.get_user(f).screen_name))
                time.sleep(10)
                unfollow_cnt += 1
            else:
                print('Reached 50 unfllow limit')
                break
    return unfollow_cnt


def main():
    followers = api.followers_ids(SN)
    friends = api.friends_ids(SN)
    unfollow(api, followers, friends)

if __name__ == '__main__':
    main()
