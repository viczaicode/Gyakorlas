def bekeres():
    ertekeles = -1
    nap = str(input("Hét napja: "))
    ora = str(input("Óra neve: "))
    ertekeles = int(input("Értékelés (0-5): "))
    while not (ertekeles >= 0 and  ertekeles < 6):
        print("Hibásan megadott adatok")
        ertekeles = int(input("Értékelés (0-5): "))
    return nap, ora, ertekeles

def kiiras(nap:str, ora:str, ertekeles:int):
    print("Köszönjük az értékelést!")
    print(f"Összefoglaló: {nap}, {ora}, {ertekeles}")