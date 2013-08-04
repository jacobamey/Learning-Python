import time
import tweepy
import urllib.request


def send_to_twitter(msg):
    CONSUMER_KEY = 'place key here'
    CONSUMER_SECRET = 'place secret here'
    ACCESS_KEY = 'place key here'
    ACCESS_SECRET = 'place secret here'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(msg)


def get_price():
    page = urllib.request.urlopen("http://www.beans-r-us.biz/prices.html")
    text = page.read().decode("utf8")
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return float(text[start_of_price:end_of_price])

price_now = input("Do you want to see the price now (Y/N)? ")

if price_now == "Y":
    send_to_twitter(get_price())

else:
    price = 99.99
    while price > 4.74:
        time.sleep(5)
        price = get_price()
    send_to_twitter("Buy!")