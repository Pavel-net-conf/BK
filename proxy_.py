
import requests
from lxml import html


class Proxy(object): 
    proxy_url = 'https://www.ip-adress.com/proxy-list'
    proxy_list = []

    def __init__(self):
        r = requests.get(self.proxy_url)
        str = html.fromstring(r.content)
        result = str.xpath("/html/body/main/table/tbody/tr[1]") 
        print(result)       
        self.proxy_list = result
        print(self.proxy_list)
    def get_proxy(self):
        for proxy in self.proxy_list:
            print(proxy)
            url = 'http://' + proxy
            try:
                r = requests.get('http://ya.ru', proxies = {'http': url})
                if r.status_code == 200:
                    return url
            except requests.exceptions.ConnectionError:
                continue

proxy = Proxy()
proxy = proxy.get_proxy()
print(proxy)



