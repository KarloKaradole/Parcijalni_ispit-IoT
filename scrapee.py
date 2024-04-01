import requests
from bs4 import BeautifulSoup

url = 'https://meteostat.net/en/place/hr/sibenik?s=14438&t=2024-04-01/2024-04-01'

response = requests.get(url)

web_site_data = BeautifulSoup(response.content, 'html.parser')

data = web_site_data.find_all('div', class_="mt-3")

print(data)