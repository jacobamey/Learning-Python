__author__ = 'Jacob Amey'

import urllib.request

page = urllib.request.urlopen("http://beans-r-us.biz/prices.html")
text = page.read().decode("utf8")

print(text)