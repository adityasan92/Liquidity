import urllib
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent','chrome')]
term = "apple stock news".replace(" ", "+")
query = "http://www.google.ca/search?q="+ term

htmltext = br.open(query).read()
print htmltext

soup = BeautifulSoup(htmltext,"lxml")

search  = soup.findAll('div',attrs={'id':'search'})

print search[0]
