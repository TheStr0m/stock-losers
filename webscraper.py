import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json

my_url="https://www.avanza.se/aktier/vinnare-forlorare.html"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup= soup(page_html,"html.parser")

stocks=[]
starttag='['
endtag=']'
table= page_soup.select("tbody")[1]
for row in table.find_all("tr"):
    priceElement = (row.select("td.lastPrice span"))
    price = float((priceElement[0].text).replace(",","."))
    if price>1:
        nameElement = (row.select("td.instrumentName span a"))
        name = (nameElement[0].get("title","no title"))
        percElement = (row.select("td.changePercent"))
        perc = float((percElement[0].text).replace(",","."))
        stocks.append([name,perc,price])
data=open("data.json","w")
data.write("")
data.close()

for stock in stocks:
    stockjson={
        "name":stock[0],
        "perc":(str(stock[1])+"%"),
        "price":stock[2],
    }

    stockjson=json.dumps(stockjson)
    data = open("data.json","a+")
    if stock == stocks[0]:
        data.write(starttag)
        data.write(stockjson)
    elif stock == stocks[-1]:
        data.write(",\n"+stockjson)
        data.write(endtag)
    else:
        data.write(",\n"+stockjson)
    data.close()