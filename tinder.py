import requests

url = 'https://tinder.com/@'

f = open('female.txt', 'r').readlines()

x = [x.strip() for x in f]

for xx in x:
	r = requests.get(url+xx)
	if f'/@{xx}' in r.text:
		print(url+xx)
		f = open('urls.txt', 'a')
		f.write(url+xx+"\n")
		f.close()