import requests
from bs4 import BeautifulSoup

url = "https://www.bing.com"

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

blah = soup.find_all(text="Search")

print(blah.prettify())
