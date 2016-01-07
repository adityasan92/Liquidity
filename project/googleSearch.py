import urllib
import mechanize
from bs4 import BeautifulSoup
import re

def getGoogleLinks(text,depth):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent','chrome')]
    term = text.replace(" ", "+")
    if depth:
        query = "http://www.google.ca/search?num=100&q="+ term + "&start=" + depth
    else:
        query = "http://www.google.ca/search?num=100&q="+ term

    htmltext = br.open(query).read()
    #print htmltext

    soup = BeautifulSoup(htmltext,"lxml")

    search  = soup.findAll('div',attrs={'id':'search'})

    searchtext =  str(search[0])

    soup1 =  BeautifulSoup(searchtext,"lxml")
    listItems = soup1.findAll('li')
    regex="http(?!.*http).*?&amp"
    pattern = re.compile(regex)

    results_Array =[]

    #print listItems[0]
    for li in listItems:
        soup2 = BeautifulSoup(str(li),"lxml")
        links = soup2.findAll('a')
        #print links
        try:
            source_link = links[0]
            source_url = re.findall(pattern,str(source_link))
            if len(source_url)> 0:
                results_Array.append(str(source_url[0].replace("&amp","")))
        except:
            continue
        #print source_link

    return results_Array

def getLinksRecursive(term,depth):
    i=0
    results_array=[]
    while i<depth:
        results_array.append(getGoogleLinks(term,str(depth*100)))
        i+=1
    return results_array

print getLinksRecursive("Amazon stock news", 3)
