import urllib.request

def get_price():
	page = urllib.request.urlopen("http://beans-r-us.biz/prices-loyalty.html")
	text = page.read().decode("utf8")
	where = text.find(">$")
	start_of_price = where + 2
	end_of_price = start_of_price + 4
	print(text[start_of_price:end_of_price])

get_price()
