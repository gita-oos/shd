'''
krasa=input("ievadi R/G/B: ")
if krasa=="sarkana":
    print("sarkana")
elif krasa== "žaļa":
    print ("žaļa")
elif krasa=="zila":
    print ( "zila")
else:
    print( "cita krasa")
    '''
'''
    #2
p=input("saule/lietus: ")
if p=="saule" or p=="Saule":
    print( "iesim caur park")
elif p=="lietus" or p=="Lietus":
    print( "iesim caur pilsētai")


else:
    print( "nesapratu!")
'''
'''
#3
skaitlis=float(input( "uzmini skaitli: "))
if skaitlis==65:
    print("uzvareji!")
else:
    print("neizdevas!")
'''

#uzd4
'''
a=input("vai ir piena jā/nē")

if a=="jā" or a=="jē":

    print("edisi parslas ar pienu")

elif a=="nā" or a=="nē":

    print("edisi sviestmaizes")

else:
    print("nesapratu!")

'''
#uzd5
'''
mac_pr=input(" izvelis kimija / spoets / muzika / fizika:  ")
if mac_pr=="kimija":
    print("tev patik kimija")

elif mac_pr=="spoets":
        print("tev patik spoets")

elif mac_pr=="muzika":
 print("tev patik muzika")

elif mac_pr=="fizika":
 print("tev patik fizika")

else:
 print("nekas nav interesants")
'''
#uzd6
'''
budžets=float(input("ievadi savu budžetu"))
if budžets<0:
    print("vel jaiekrai")
elif budžets<500 and budžets>0 :
    print("celo uz bulgariju")
elif budžets >=500 and budžets<1000:
    print("celo uz angliju")
else:
    print("vel padoma kur gribi celot")
'''
#uzd7
'''
garastavoklis=input("garastavoklis labs/slikts")
if garastavoklis=="labs" :
    print("klaisamies iecienito muziku")
elif garastavoklis=="slikts" :
    print("klaisamies relaksejoso muziku")

else:
    print("kludaina ievade")

'''
#uzd8
'''
Augs=input("augs slims/vesals")
if Augs=="slims":
    print("tad laistam Augu")
elif  Augs=="vesals":
    print("tad rave nezales")
else:
    print("kludaina ievade")
'''
'''
#uzd9
nauda=float("inputcik ir nauda"))
pirkums=float(input("cik maksa pirkums"))
if nauda>=pirkums:
    print("preci var nopirkt, paliks pari{ nauda -pirkums} eiro ")
elif pirkums>nauda:
    print('vel jakrai { pirkums - nauda} ")
else:
    print("kludaina ievade")
'''
#uzd10
'''
import math
x=int(input("ievadi bralu skaitu"))
y=int(input("ievadi konfesu skaitu" ))
c=y/x
print(math.floor(c))
m=y%x
print(m)
'''
#uzd11
'''
import math
c=300000000
m=float(input("Īevadi masu"))
E=m*c**2
E=m*math.pow(c,2)
print("E=",E,"dzouli")
'''
#uzd12
'''
x,y,z=input("Īevadi izsteiksmi: ").split()
x=int(x)
z=int(z)
if y=="+":
    print(f"skaitlu summa ir {(x+z):.if}")
elif y == "-":
        print(f"skaitlu starpiba ir {(x - z):.if}")
elif y == "*":
        print(f"skaitlu r ir {(x * z):.if}")
if y == "/":
        print(f"skaitlu d ir {(x / z):.if}")
else: 
    print("ievadi nezinamo skaitli")
'''
#uzd13
'''
for k in range(55,33,-3):
    print(k)
'''
'''
sum=0
for k in range(8):
    sk=int(input("sk="))
    sum+=sk
print(sk)
'''
'''
import math
for x in range(1,10):
    y=math.pow(x ,2)+3*x-2
    print(f"ja x={x}, tad y={y}")
'''

'''
import math

D=int(input("cik jabut dekoracijau"))
D_m=float(input("cik maksa dekoracijas"))
A=float(input("cik maksa animators"))
T_n=float(input("cik maksa telpas noma"))

kopsumma=T_n+A+D_m*10
print(f"organizacija cena ir {kopsumma}")
'''
'''
a=12
b=2
def saskaitisana (a,b):
    return a+b
saskaitisana (a,b)
print(saskaitisana (a,b))

def atnemsana(a,c=13) :
    print(a-c)
atnemsana(a)

def reizinasana(a,b):
    return a*b
print(reizinasana(a,b))

def dalisana(a,b):
    print(a/b)
    dalisana(a,b)

izvele=input("izveles +,-,*,/ ")
if izvele=="+":
    print(saskaitisana(a,b))
elif izvele=="-":
    atnemsana(a)
elif izvele == "*":
    print(reizinasana(a, b))
elif izvele == "/":
    dalisana(a,b)
    print("kluda!")
'''
'''
sk=int(input("sk= "))
def skaitlis(sk):
    if sk %2==0:
        print("para skaitlis")
    else:
        print("nepara")
skaitlis(sk)
'''
'''
m=int(input("masa: "))
c=300000000

def Einstein(m,c):
    e=m*c**2
    print(e,"džouli")
Einstein(m,c)
'''
'''
maltites_izm=float(input("cik jamaksa"))
procenti=int(input("10,15, citi%?"))
def dzeramnauda(maltites_izm, procenti):
    summa=maltites_izm*procenti/100
    print(summa,"eiro")

dzeramnauda(maltites_izm, procenti)
'''
'''

zime=input("izveles :(, :), :/,:^:0,:}")

def concvert(zime):
    if zime==":)":
        print ("🌞")
    elif zime==":(":
       print("⛅")
    elif zime==":/":
       print("🗿")
    elif zime==":^":
       print("💏")
    elif zime==":0":
       print("🎭")
    elif zime==":}":
       print("🎃")
    else:
       print("kluda!")
concvert(zime)
'''
'''

for k in range (10):
    print(k+1)
'''
'''
for i in range(20,0,-1):
    print(i)
'''
'''
for x in range(1,10):
    y=x**2+3*x-2
    print(f'ja x{x}, tad y{y}'v )

    '''
'''
import random
x=random.randint(0,8)
print(x)
'''
'''
import random

m=int(input("m:"))
for i in range(m):
    sk=random.randint(0,60)
    print(i+1,".",sk)


    for i in range(m,0-1,-1):
        sk = random.randint(0, 60)
        print(f'{i}.{sk}')
'''
'''
c=int(input("skaitlu skaits:"))
summa=0
for k in range(c):
    sk=int(input("sk: "))
    summa+=sk
    print(summa)
print("sum=",summa)
'''
'''
import math
for n in range(7,13):
    #print(n**2)
print(math.pow( n ,2))
'''
'''
import math
for k in range(27,17,-1):
    print(math.sqrt(k))
print(k**0.5)
'''
'''

for i in range(1,50):
    if i%3==0 or i%5==0:
        print(i)
    else:
        print("nedalas ar 3 ub 5")
'''
'''
n=int(input("n: "))
for i in range(1,n):
    print(i,i**2)
else:
    for i in range(n,1):
        print(i, i ** 2)
'''
'''

for k in range ( 1 ,20):
    if k%2==0:
        continue
    else:
        print(k,"ir nepara")



n=int(input("n: "))
sum=0
for i in range(n):
    sk=int(input("sk: "))
    if sk>0:
        sum+=sk
    else:
        break
print("pozitivs skaitlis", sum)

'''
'''
for i in range(n)
    if i%3==0 or i%5==0:
        print(n)
    else:
        print("nedalas ar 3 VAI 5")
'''

'''
while True:#bezgalīgais cikls
sk=int(input("sk= "))
if sk%3==0 or sk%5==0:
break
elif sk%4==0:
continue
else:
print("nedalas ar 3, 4 vai 5")
'''
'''
k=int(input("k= "))
n=int(input("n= "))

while k<=n:
print(n)
k+=1
'''
'''
k=int(input("k= "))
n=int(input("n= "))
if k>n:
while k>n:
print(k)
elif n>k:
while n>k:
print(n)
else:
print(k=n)
'''
'''
m=int(input("m= "))
s=0
while s sk=random.randint(0,20)
print(sk)
s+=1
'''
'''
lats=1.42
latu_skaits=float(input("ievadi latu apjomu"))
def pelmenis(lats, latu_skaits):
       print(f'{lats*latu_skaits:.2f}eur.')

pelmenis(lats,latu_skaits)

'''

'''
kola=0.50
summa=0

def automats(kola, summa):

    while summa<=50:
        nauda=int(input("naudas APJOMS"))


    if nauda==20  or nauda==10 or nauda==5
     '''

v=input("ievadi virkni: ")
'''

v3=''
for i in range(len(v)):
    if v[i]=="a" or v[i]=="e" or v[i]=="i" or v[i]=="o" or v[i]=="u":
         v3+=""
    else:
         v3+=v[i]

print(v3)
  '''
'''
s=input("iev virk: ")
print(s.replace(" ", "..."))
print(s)

  '''
'''
v='thequickbrownfoxjumpsoverthelazydog'
print(v[::2])

print(v[::-1])

print(v[::-2])

print(v.count("the"))

print(v.replace( "a", "d"))
  '''
'''
v=input("ievadi virkni: ")
def garums(v):
   if len(v)<5:
     print(v)
   else:
       print(v[0],v[1],v[-2],v[-1])
garums(v)
  '''
'''
v1=input("ievadi virkni viens: ")
v2=input("ievadi vieknui divi: ")
print(len(v1))
print(len(v2))

if len(v1)>len(v2):
    for i in range(len(v1)):
        print(v1[i])
elif len(v1)<len(v2):
    for i in range(len(v2)):
        print(v2[i])
else:
        print("vieknes ir vienadas")
 '''

v=input("iv vi:")







































