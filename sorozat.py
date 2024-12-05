import random

def randomSzamok():
    szamok_lista = []
    for i in range(0,7,1):
        szam = random.randint(-100,859)
        szamok_lista.append(szam)
    return szamok_lista

def listaKiiratas(szamok_lista):
    for i in range(len(szamok_lista)):
        szam = szamok_lista[i]
        if i < len(szamok_lista) - 1:
            print(szam, end=";")
        else:
            print(szam)

def tizzel_osztahatoak_szama(szamok_lista):
    szamlalo = 0
    for i in range(len(szamok_lista)):
        szam = szamok_lista[i]
        if szam % 10 == 0:
            szamlalo += 1
    return szamlalo

def konzol_ir(szamlalo):
    print(f"Tízzel osztható számok száma: {szamlalo}")

def fajlba_ir(szamlalo):
    fajlom = open("vegeredmeny.txt", "w", encoding='UTF-8')
    fajlom.write(f"Tízzel osztható számok száma: {szamlalo}")
    fajlom.close