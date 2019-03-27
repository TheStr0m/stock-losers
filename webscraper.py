import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url="https://www.avanza.se/aktier/vinnare-forlorare.html"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup= soup(page_html,"html.parser")

stocks=[]

table= page_soup.select("tbody")[1]

for row in table.find_all("tr"):
    nameElement = (row.select("td.instrumentName span a"))
    name = (nameElement[0].get("title","no title"))
    percElement = (row.select("td.changePercent"))
    perc = (percElement[0].text)
    priceElement = (row.select("td.lastPrice span"))
    price = (priceElement[0].text)
    stocks.append([name,perc,price])
print(stocks)