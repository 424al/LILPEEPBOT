import tweepy
from linereader import copen
from random import randint
import time

#import twitter apps configaration file from config.py file
from config import *

#Authentication using keys & accesstoken
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

lyrics = copen('lyrics.txt')
lines = lyrics.count('\n')
lastline = 0

while True:
    gottenline = randint(1, lines)
    while gottenline == lastline:
	gottenline = randint(1, lines)
    tweet_text = lyrics.getline(gottenline)
    if len(tweet_text) <= 140 and tweet_text != '\n':
	tweet_text = tweet_text.replace("|", '\n')
	api.update_status(status=tweet_text)
	print tweet_text
	time.sleep(3600)