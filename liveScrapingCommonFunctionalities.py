import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

def getPage(address):
    try:
        html = urlopen(address)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print('The server could not be found!')
    else:
        print('Html initialized safely!')
        return BeautifulSoup(html.read(), "html.parser")