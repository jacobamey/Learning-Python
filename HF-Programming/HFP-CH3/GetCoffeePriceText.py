import time
import smtplib
import urllib.request

username = "account@gmail.com"
password = "password"
vtext = "number@vtext.com"


def get_price():
    page = urllib.request.urlopen("http://beans-r-us.biz/prices-loyalty.html")
    text = page.read().decode("utf8")
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return float(text[start_of_price:end_of_price])

i = str(get_price())
message = i + " - Buy Coffee"


def send_to_text():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, vtext, message)
    server.quit()


price_now = input("Do you want to see the price now (Y/N)? ")

if price_now == "Y":
    send_to_text()

else:
    price = 99.99
    while price > 4.74:
        time.sleep(5)
        price = get_price()
    send_to_text()