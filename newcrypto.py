import requests


url = f'https://coinmarketcap.com/new/'
	
response = requests.get(url)

if response.status_code == 200:
	html = response.text
	for i in html.split('<tr style="cursor:pointer">'):
		if "Own Blockchain" in i:
			name = i.split("</p>")[1].split('>')[-1]
			if "IOU" not in name:
				print(name)