import urllib2

url = "https://mtgox.com/api/1/BTCUSD/ticker"



headers = { 'User-Agent' : 'Mozilla/5.0' }
req = urllib2.Request(url, None, headers)
data = urllib2.urlopen(req).read()

print data.split("\"last\":{\"value\":\"")[1].split("\",\"")[0]
