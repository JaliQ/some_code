import json
from datetime import datetime


def check_time(date1,date2,date3):
    if (date1>= date3) and (date1<=date2):
        return True
    return False
def check_price(price1,price2,price3):
    if (price1>= price3) and (price1<= price2):
        return True
    return False
inp = input()
data = json.loads(inp)
filters = {}
for i in range(5):
    name,value = list(input().split())
    filters[name] = value
results =[]
dayb = int(filters['DATE_BEFORE'][0:2] if filters['DATE_BEFORE'][0]!=0 else filters['DATE_BEFORE'][1:2]  )
monthb = int(filters['DATE_BEFORE'][3:5] if filters['DATE_BEFORE'][3]!=0 else filters['DATE_BEFORE'][4:5]  )
yearb = int(filters['DATE_BEFORE'][6:10])
dateb = datetime(yearb,monthb,dayb) #date before
daya = int(filters['DATE_AFTER'][0:2] if filters['DATE_AFTER'][0]!=0 else filters['DATE_AFTER'][1:2])
montha = int(filters['DATE_AFTER'][3:5] if filters['DATE_AFTER'][3]!=0 else filters['DATE_AFTER'][4:5])
yeara = int(filters['DATE_AFTER'][6:10])
datea = datetime(yeara, montha, daya)
pricel = int(filters['PRICE_LESS_THAN'])
priceg = int(filters['PRICE_GREATER_THAN'])
name_cont = filters['NAME_CONTAINS']
#NAME_CONTAINS, PRICE_GREATER_THAN, PRICE_LESS_THAN, DATE_BEFORE, DATE_AFTER

for i in data:
    month = int(i["date"][3:5] if i["date"][3]!="0" else i["date"][4:5])
    day = int(i["date"][0:2] if i["date"][0]!="0" else i["date"][1:2])
    date =datetime(int(i["date"][6:10]),month, day)
    if check_time(date,dateb,datea):
        price = int(i["price"])
        if check_price(price,pricel,priceg):
            name = i["name"]
            if name_cont.lower() in name.lower():
                results.append(i)
results = sorted(results,key =  lambda x : x["id"])
print(results)