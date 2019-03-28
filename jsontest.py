import json

stocks={
    "name":"tingo",
    "age":"bingo"
}

with open("data.json","w") as outfile:
    json.dump(stocks,outfile)