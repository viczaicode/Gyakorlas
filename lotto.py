from hatoslotto import Hatoslotto

def beolvas(fajlnev):
    huzasok_lista=[]
    fajlom = open(fajlnev,"r", encoding="UTF-8")
    elso_sor = fajlom.readline()
    tobbi_sor_lista = fajlom.readlines()

    for i in range(len(tobbi_sor_lista)):
        sor = tobbi_sor_lista[i].strip()
        sor_lista = sor.split("@")
        huzas = Hatoslotto(sor_lista[0], sor_lista[1], sor_lista[2], sor_lista[3])
        #print(huzas)
        huzasok_lista.append(huzas)
    fajlom.close()
    return huzasok_lista, huzas

def hanyHuzas(huzasok_lista):
    huzasok_szama = len(huzasok_lista)
    print(f"A húzások száma: {huzasok_szama}")

def huzasAtlag(huzasok_lista, huzas):
    kivalasztotthuzasok = []
    het_szama = 43
    for i in range(len(huzasok_lista)):
        if huzasok_lista[i].het == het_szama:
            kivalasztotthuzasok.append(huzasok_lista[i].szam)
            #print(huzasok_lista[i].szam)
    return kivalasztotthuzasok

def huzasOsszSzamolas(kivalasztotthuzasok):
    ossz = 0
    for i in range(len(kivalasztotthuzasok)):
        ossz += i
    return ossz

def atlag(kivalasztottszamok, ossz):
    veglegesatlag = ossz / len(kivalasztottszamok)
    return veglegesatlag



def huzasAtlagKiiras(veglegesatlag):
    print(f"A 43. héten húzott számok átlaga: {veglegesatlag}")


def legnagyobbHuzas(huzasok_lista):
    legnagyobb = 0
    for i in range(len(huzasok_lista)):
        if huzasok_lista[i].szam > legnagyobb:
            legnagyobb = huzasok_lista[i].szam
            ev = huzasok_lista[i].ev
            het = huzasok_lista[i].het
            huzas = huzasok_lista[i].huzas

    return legnagyobb, ev, het, huzas

def legnagyobbHuzasKiiras(legnagyobb, ev, het, huzas):
    print(f"Az első legnagyobb kihúzott szám értéke: {legnagyobb}, {ev}-ban/ben, a {het}. héten húzták ki, ez volt a {huzas}. húzás")
