import random

#0
print("tanuló adatai ömlesztve")

#1
adatsorbe=input("kérem a tanuló adatait';'-el elválasztva: ")

reszleteket = adatsorbe.split(';')

tanulo={}
tanulo["nev"]=reszleteket[0]
tanulo["szid"]=reszleteket[1]
tanulo["magasag"]=int(reszleteket[2])
tanulo["tomeg"]=float(reszleteket[3].replace(',' , '.'))

#2
tanulo['nev']="Váradi László"
tanulo["szid"]=str(random.randint(2000,2005))+'.'+str(random.randint(2000,2010))+'.'+str(random.randint(1,12))+'.'str(random.randint(1,28))
tanulo["magasag"]=random.randint(150,220)
tanulo["tomeg"]=random.randint(50,110) + random.random()

#3
reszleteket[0]=tanulo["nev"]
reszleteket[1]=tanulo["szid"]
reszleteket[2]=str(tanulo["magasag"])
reszleteket[3]=str(tanulo["tomeg"])
adatsorki = '#'.join(reszleteket)
print(adatsorki)