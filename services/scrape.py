import requests
from bs4 import BeautifulSoup


URL = 'https://www.worldometers.info/coronavirus/'
response = requests.get(URL)

web_site_data = BeautifulSoup(response.content, 'html.parser')

data = web_site_data.find_all('div', id="maincounter-wrap")

# print(data[0])
title = data[2].find('h1').get_text()
cases = data[2].find('span').get_text()
print(title, cases)