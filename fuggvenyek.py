def etlap(lista):
    for i in range(0,len(lista),1):
        print(f"** {lista[i].nev} ár: {lista[i].ar:>8}Ft **")

def atlag(lista):
    osszes = 0
    for i in range(0,len(lista),1):
        osszes += (lista[i].ar)
    atlag = osszes / len(lista)
    return atlag

def legdragabb(lista):
    max_index = 0
    for i in range(0,len(lista),1):
        if (lista[max_index].ar) < (lista[i].ar):
            max_index = i
    print(f"A legdrágább étel: {lista[max_index].nev}\nÁra: {lista[max_index].ar} Ft")

def feladat1(lista):
    osszes = 0
    for i in range(0,len(lista),1):
        osszes += lista[i].fizetes
    return osszes

def feladat2(lista):
    max_index = 0
    for i in range(0,len(lista),1):
        if (lista[max_index].kor) < (lista[i].kor):
            max_index = i
    print(f"A legidősebb alkalmazott: {lista[max_index].nev}, aki {lista[max_index].kor} éves")

def feladat3(lista):
    beosztottak = 0
    for i in range(0,len(lista),1):
        if lista[i].pozicio == "Beosztott":
            beosztottak += 1
    return beosztottak

def feladat4(lista):
    min_index = 0
    for i in range(0,len(lista),1):
        if (lista[min_index].fizetes) > (lista[i].fizetes):
            min_index = i
    print(f"A legkevesebb fizetést {lista[min_index].nev} kapja, ami: {lista[min_index].fizetes} fabatka")

def fizetesemeles(lista,emeles):
    emel = emeles*0.1
    fizuk = []
    min_index = 0
    for i in range(0,len(lista),1):
        if (lista[min_index].fizetes) > (lista[i].fizetes):
            legkisebb = (lista[min_index].fizetes) + ((lista[min_index].fizetes)*0.2) 
            fizuk.append(legkisebb)
        else:
            megemel = (lista[i].fizetes) + ((lista[i].fizetes)*emel)
            fizuk.append(megemel)
    print("Új fizetések: ")
    for o in range(0,len(lista),1):
        print(f"{lista[o].nev} --- {fizuk[o]} fabatka")