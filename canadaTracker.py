import requests
import csv
from tkinter import *

response = requests.get("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv");

parsed = response.content.decode('utf-8')
csveed = csv.reader(parsed.splitlines(), delimiter=',')

cg = list(csveed)
jk = list()
countries = set()
total = list()
totalval =0

for i in range(len(cg)):
    if i == 0: continue
    hjk = list(cg[i])
    countries.add(hjk[1])

    o = list()
    o.append(hjk[-1])
    total.append(o[-1])


for i in total:
    if "/" in i: continue
    totalval = totalval + int(i)

list(countries)


#GUI--------------------------------

root = Tk()
scroll = Scrollbar(root)
root.title("Canada")
lsit = Listbox(root, yscrollcommand = scroll.set(0,50), bg="black", fg="white", width =40 , height= 18)

#------------------------------------

detail = list()

for i in countries:
    detail.append([i,0])

date = cg[0][-1]
cnd = 0
for i in range(len(detail)):
    if i == 0:  continue
    ct = list()
    ct.append(detail[i][0])
    for j in cg:
        k = list()
        k.append(j[1])
        bn = j[-1]

        if 'Country/Region' in ct:
            continue

        if k==ct:
            if j[1] == "Canada":
                print(j[0] + " : "+ str(int(bn)))
                lsit.insert(END,j[0] + " : "+ str(int(bn)))
                cnd = cnd + int(bn)


lsit.insert(END,"")
lsit.insert(END,"> CANADA : "+str(cnd))
print("\n------------------- \nCanada : "+str(cnd))




lsit.pack(side="left")

scroll.config(command=lsit.yview())
root.mainloop()










