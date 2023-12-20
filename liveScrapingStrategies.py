import requests
from bs4 import BeautifulSoup

from liveScrapingTyping import *

def getPage(url):
    try:
        req = requests.get(url)
    except requests.exceptions.RequestException:
        return None
    return BeautifulSoup(req.text, 'html.parser')

def getTextOfFirstTagMatchedInSoup(searchPattern, bs, property = "tag"):
    try:
        title = bs.find(**searchPattern).text
    except AttributeError as e:
        print(f"An attempt was made to access the text of the assumed to be {property}, None was accessed.")
        return ''
    return title

def searchForTextOfFirstMatch(url : Url, pattern : Pattern):
    bs = getPage(url)
    tag = getTextOfFirstTagMatchedInSoup(pattern, bs)
    return tag

def searchForTagByParts(url, pattern : Pattern):
    tags = getPage(url).find_all(**pattern)
    goalTag = ''
    for tag in tags:
        goalTag += (tag.text) + "\n"
    return goalTag

def justReturnTheUrl(url, pattern : Pattern):
    return url

BrookingsStrategy = {
    "url"   : justReturnTheUrl,
    "title" : searchForTextOfFirstMatch, 
    "body"  : searchForTagByParts
    }

NYTimesStrategy = {
    "url"   : justReturnTheUrl,
    "title" : searchForTextOfFirstMatch,
    "body" : searchForTagByParts
}
strategies = {
    "brookings.edu"  : BrookingsStrategy,
    "nytimes.com"   :NYTimesStrategy
}