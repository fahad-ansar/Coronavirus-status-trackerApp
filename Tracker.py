import requests
import csv

response = requests.get("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv");
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


detail = list()

for i in countries:
    detail.append([i,0])

date = cg[0][-1]

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
            detail[i][1] = detail[i][1] + int(bn)






for i in detail:
    print(i[0] + " :  " + str(i[1]))

print("As of today " + str(date) + ": \n")
print("Total Cases: " + str(totalval))

