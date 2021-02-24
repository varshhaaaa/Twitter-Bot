import tweepy
import time

consumer_key = 'kE2qq7ohVqGweMfocIdGklYCD'
consumer_secret = 'x8eNbJZPCjEbwYPsOnI595Rh0kwNepTpEVk8TXgkImAKZIIBZ4'
key = '1343157111115669505-YswG3Fcb85enjoCi6rhabUsYfGJOxh'
secret = 's3uMBXHBQEbFKcIeGylGZfcxBif0O9t2z6k8VZNaqHDft'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

#api.update_status('Hello from twitter bot-2nd tweet')

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#randomtweet' in tweet.full_text.lower():
            print('Replied to ID - ' + str(tweet.id))
            api.update_status('@' + tweet.user.screen_name + " Hlo Hlo", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(15)
