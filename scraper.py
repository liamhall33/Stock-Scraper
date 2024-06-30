import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
url = 'https://finance.yahoo.com/quote/PLTR'

r = requests.get(url)

print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')

print(soup.title.text)

parent = soup.find('fin-streamer',{'class':'livePrice svelte-mgkamr'})

target = parent.contents[0]
value = target.text
print('Stock price:', value)


