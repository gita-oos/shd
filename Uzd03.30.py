import csv

datne=open("kontakti.csv",encoding="utf-8")
saturs=list(csv.reader(datne))
datne.close()
print(saturs)
for cilveks in saturs:
    print(cilveks[0],"\t",cilveks[-1])

galvene=["vards","Ūzvards","telefons","pilseta"]

with open("k1.csv","w",encoding="utf-8",newline="") as fails:
    c=csv.writer(fails, delimiter="\t")
    c.writerows(galvene)
    c.writerows(saturs)
    print(galvene,"\t",saturs)