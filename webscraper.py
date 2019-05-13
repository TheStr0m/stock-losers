#Importing libraries and declaring variables
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json
import time
my_url="https://www.avanza.se/aktier/vinnare-forlorare.html"
myStocks=[]
starttag='['
endtag=']'
myJsonFile="data.json"
myTable=""

def webLoad(url):
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup= soup(page_html,"html.parser")
    try:
        table= page_soup.select("tbody")[1]
    except:
        time.sleep(900)
    table= page_soup.select("tbody")[1]
    return table


#Picking out interesting data
def dataPick(table):
    stocks=[]
    for row in table.find_all("tr"):
        priceElement = (row.select("td.lastPrice span"))
        price = float((priceElement[0].text).replace(",","."))
        if price>1:
            nameElement = (row.select("td.instrumentName span a"))
            name = (nameElement[0].get("title","no title"))
            percElement = (row.select("td.changePercent"))
            perc = float((percElement[0].text).replace(",","."))
            stocks.append([name,perc,price]
    return stocks

#Writing to JSON
def writeToJson(jsonFile,array):
    data=open(jsonFile,"w")
    data.write("")
    data.close()
    for stock in array:
        stockjson={
            "name":stock[0],
            "perc":(str(stock[1])+"%"),
            "price":stock[2],
        }

        stockjson=json.dumps(stockjson)
        data = open("data.json","a+")
        if stock == array[0]:
            data.write(starttag)
            data.write(stockjson)
        elif stock == array[-1]:
            data.write(",\n"+stockjson)
            data.write(endtag)
        else:
            data.write(",\n"+stockjson)
        data.close()

while True:
    myStocks=[]
    myTable=webLoad(my_url)
    myStocks=dataPick(myTable)
    writeToJson(myJsonFile,myStocks)
    time.sleep(300)
