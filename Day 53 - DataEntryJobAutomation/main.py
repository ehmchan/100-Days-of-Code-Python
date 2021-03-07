from bs4 import BeautifulSoup
import requests
import os

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
head = {
    "Accept-Language": os.environ["Accept_Language"],
    "User-Agent": os.environ["User_Agent"]
}

response = requests.get(url=ZILLOW_URL, headers=head)
zillow_webpage = response.text
soup = BeautifulSoup(zillow_webpage, "html.parser")

all_links = soup.find_all("div", class_="list-card-info")
links = []
for l in all_links:
    link = l.find("a", class_="list-card-link")
    if "/b/" in link.get('href'):
        links.append(f"https://www.zillow.com{link.get('href')}")
    else:
        links.append(link.get('href'))

all_prices = soup.select("div.list-card-price")
prices = []
for p in all_prices:
    if '+' in p.getText():
        price = p.getText().split('+')[0]
        prices.append(price)
    elif '/' in p.getText():
        price = p.getText().split('/')[0]
        prices.append(price)
    elif ' ' in p.getText():
        price = p.getText().split(' ')[0]
        prices.append(price)
    else:
        prices.append(p.getText())

all_addresses = soup.find_all("address", class_="list-card-addr")
addresses = [address.getText() for address in all_addresses]


