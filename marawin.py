
import requests
#from requests.api import request
from bs4 import BeautifulSoup
from difflib import SequenceMatcher
from collections import defaultdict


# get text html page with requests 
def get_html(url):
    r = requests.get(url,proxies={'http': '211.24.105.19:47615'})
    print(r.status_code)
    return r.text


def get_all_event_marathonbet(html):

    soup = BeautifulSoup(html, 'html.parser')

    print(soup.find('div', id = 'events_content'))

get_all_event_marathonbet(get_html('https://www.marathonbet.ru/su/popular/Tennis+-+2398'))