import requests
from bs4 import BeautifulSoup
URL = 'https://x-1xbet-78144.world/ru/line/Tennis/'

def get_html(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else:
        print('Error!')
    

def get_all_ivents_1xbet(html):
    all_players = []
    all_k = []
    soup = BeautifulSoup(html, 'html.parser')

    all_evetns = soup.find('div', id='games_content').find_all('div', class_ = 'c-events__item c-events__item_col')
    for players in all_evetns:
        players = players.find('a', class_= 'c-events__name')
        player_1 = players.find('span', class_ = 'c-events__teams').find('span').text 
        player_2 = players.find('span', class_ = 'c-events__teams').find('span').findNext('span').text

        print(player_1)




get_all_ivents_1xbet(get_html(url=URL))