#!/usr/bin/env python
import sys
import tweepy

CONSUMER_KEY = 'place key here'
CONSUMER_SECRET = 'place secret here'
ACCESS_KEY = 'place key here'
ACCESS_SECRET = 'place secret here'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(sys.argv[1])