import tweepy

CONSUMER_KEY = 'place key here'
CONSUMER_SECRET = 'place secret here'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url()
print('Please authorize: ' + auth_url)
verifier = input('PIN: ').strip()
auth.get_access_token(verifier)
print("ACCESS_KEY = '%s'" % auth.access_token.key)
print("ACCESS_SECRET = '%s'" % auth.access_token.secret)