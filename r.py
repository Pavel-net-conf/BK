import requests 

r = requests.get('https://www.orange.es/', proxies={'http': '211.24.105.19:47615'})
print(r.status_code)