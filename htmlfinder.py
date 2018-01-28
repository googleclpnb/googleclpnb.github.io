from requests import get
from bs4 import BeautifulSoup

response = get("https://www.upstreamint.org/what-we-do")
html_soup = BeautifulSoup(response.text,"lxml")
type(html_soup)

print(html_soup)

