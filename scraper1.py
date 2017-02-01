from bs4 import BeautifulSoup
import requests

url = "http://example.com"

response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, 'lxml')

tags = soup.findAll('a')

for tag in tags:
    print(tag.get('href'))





