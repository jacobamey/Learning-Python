import twitter as t
import urllib.request as ur
import time

CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN_KEY= 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN_SECRET= 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


def tweet(status_msg):
    if len(status_msg) > 140:
        raise Exception('Status message too long !!!')
    else:
        authkey = t.Twitter(auth=t.OAuth(ACCESS_TOKEN_KEY,        ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
        result = authkey.statuses.update(status=status_msg)
        return result


def get_price(page):
    text = page.read().decode("utf8")
    ss_pos = text.find('>$')
    soss = ss_pos + 2
    eoss = soss + 4
    return float(text[soss:eoss])


print("Welcome to Starbuzz Coffee price checking program")
choice = input ("Do You want to know the coffee price immediately ?? (y/n) : ")
if choice == "y":
    page = ur.urlopen("http://beans.itcarlow.ie/prices.html")
    price = get_price(page)
    status_msg = "@starbuzzceo, Current price of coffee = $" + str(price)
    res = tweet(status_msg)
else :
    price = 99.99
    while price > 4.74 :
        time.sleep(10)
        page = ur.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
        price = get_price(page)
    status_msg = "@starbuzzceo !\nCurrent price of coffee is $" + str(price) + "; BUY !!!"
    res = tweet(status_msg)

if res != None:
    print("tweeted coffee price successfully to Starbuzz CEO")
else:
    print("problem !!")
