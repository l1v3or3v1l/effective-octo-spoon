# Steps to run
# pip install requests bs4 wget
# python tinder-pics.py

import requests
import re                                            import json                                          from bs4 import BeautifulSoup                        from sys import exit
import wget                                          import os

url = 'https://tinder.com/@'

xx = input('username : ')

r = requests.get(url+xx)                             if f'/@{xx}' not in r.text:
        exit()

soup = BeautifulSoup(r.text, 'html.parser')
script = soup.find('script', string=re.compile('window.__data'))

json_text = re.search(r'^\s*window.__data\s*=\s*({.*?})\s*;\s*$',
                      script.string, flags=re.DOTALL | re.MULTILINE).group(1)

data = json.loads(json_text)

parr = data['webProfile']['user']['photos']

os.mkdir(xx)

for p in parr:
        purl = p['processedFiles'][0]['url']
        pr = requests.get(purl, allow_redirects=True)
        open(f'{xx}/{purl.split("_")[-1]}', 'wb').write(pr.content)

print(url+xx)
