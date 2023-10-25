#Prvo zaženite skripto ustvari_JSON.py, ta vam bo generirala oba JSON dokumenta.
#Skripto dobite na naslednjem naslovu: https://github.com/Jabobu/VAJE/blob/main/DN3/ustvari_JSON2x.py

import json

#Peberite začetno datoteko JSON in jo shranite v spremenljivko, npr. zacetniData.
#Namig: Uporabite Pythonov vgrajeni modul json in metodo json.load() za branje datoteke.
with open(r'C:\Users\Jure Selšek\Documents\VSŠ FE\3.LETNIK\1. semester\TP x\github\DN3\zacetniData.json', 'r') as zacetna_file:
    zacetniData = json.load(zacetna_file)

#Peberite še datoteko JSON za posodobitev in jo shranite v drugo  spremenljivko npr updateData.
with open(r'C:\Users\Jure Selšek\Documents\VSŠ FE\3.LETNIK\1. semester\TP x\github\DN3\updateData.json', 'r') as posodobitev_file:
    updateData = json.load(posodobitev_file)

#Uporabite Pythonovo razumevanje slovarjev (dictionary comprehension), kjer ustvarimo novi slovar npr. zacetni slovar. 
#To bo omogočilo hitro iskanje in posodabljanje, ker dobimo slovar kjer je kljuc ime in vrednost so vsi podatki za to osebo.
zacetniSlovar = {oseba['name']: oseba for oseba in zacetniData['persons']}

#Z novim slovarjem in zanko `for` preglejte vse posodobitve in uporabite metodo `.update()` za posodabljanje zapisov.
#Namig: Loopamo cez updateData spremenljivko tako, da dobimo imena ven. 
#Z imeni nato preverimo ce se nahaja isto ime tudi v zacetniData spremenljivki. 
#Ce je (True) potem posodobite nas novi slovar "zacetni.slovar[ime].update(update_person)
for oseba in updateData['persons']:
    ime = oseba['name']
    if ime in zacetniSlovar:
        zacetniSlovar[ime].update(oseba)

#Pretvorite posodobljeni slovar nazaj v prvotno obliko seznama 
zacetni_slovar = list(zacetniSlovar.values())

posodobljena_datoteka = {'persons': zacetniSlovar}

#Zapišite posodobljene zapise v novo datoteko JSON
with open(r'C:\Users\Jure Selšek\Documents\VSŠ FE\3.LETNIK\1. semester\TP x\github\DN3\nova.json', 'w') as izhodna_file:
    json.dump(posodobljena_datoteka, izhodna_file, indent=2)