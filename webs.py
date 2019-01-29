from bs4 import BeautifulSoup
import requests

search = input("Enter search item")
params = {"q":search}
r = requests.get("https://www.bing.com/search", params=params)
soup = BeautifulSoup(r.text)
print(soup.prettify())
