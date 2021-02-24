import tweepy
import time

consumer_key = 'kE2qq7ohVqGweMfocIdGklYCD'
consumer_secret = 'x8eNbJZPCjEbwYPsOnI595Rh0kwNepTpEVk8TXgkImAKZIIBZ4'
key = '1343157111115669505-YswG3Fcb85enjoCi6rhabUsYfGJOxh'
secret = 's3uMBXHBQEbFKcIeGylGZfcxBif0O9t2z6k8VZNaqHDft'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag = "100daysofcode"
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchbot()
