url = "https://www.bing.com"

from bs4 import BeautifulSoup
soup = BeautifulSoup(url, 'html.parser')
print(soup.prettify())
