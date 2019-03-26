import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url="https://www.avanza.se/aktier/vinnare-forlorare.html"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup= soup(page_html,"html.parser")

class stock:
    def __init__(self, name, perc, price):
        self.name=name
        self.perc=perc
        self.price=price

table= page_soup.select("tbody")[1]

for row in table.find_all("tr"):
    print(row.select("td#instrumentName > span > a"}))