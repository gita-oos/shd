import json
datne=open("uzd3.json",encoding="utf=8")
dati=json.load(datne)
uznemumi=[]
vid_cena=[]
uznemumi.append("Apple Inc.")
print(uznemumi)

for vardnica in dati:
  print(vardnica["NASDAQ"])


for vardnica in dati:
      print(vardnica["NYSE"])

for vardnica in dati:
      print(vardnica["Nasdaq Riga"])


vid=(vardnica["NASDAQ"]+vardnica["NYSE"]+vardnica["Nasdaq Riga"])/3


import csv

csv.weiter=open("akciju_analize.csv",encoding="utf=8")