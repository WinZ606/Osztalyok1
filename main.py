from Alkalmazottak import Alkalmazottak
from etel import Etel
import fuggvenyek

#1.
"""etel_lista = []
etel_lista.append(Etel("húsleves",1234))
etel_lista.append(Etel("krumplis",2345))
etel_lista.append(Etel("rántott hús",2154))
etel_lista.append(Etel("palacsinta",1450))"""

"""fuggvenyek.etlap(etel_lista)
atlag_ar = fuggvenyek.atlag(etel_lista)
print(f"Átlag ár: {atlag_ar}Ft ")
fuggvenyek.legdragabb(etel_lista)"""

#2.
alkalmazott = []
alkalmazott.append(Alkalmazottak("Ember1",2000,350,"Beosztott"))
alkalmazott.append(Alkalmazottak("Lakatos Strandkorlát",1999,200,"Takarító"))
alkalmazott.append(Alkalmazottak("Dr. Ombi Ferenc",1998,450,"Ügyvezető"))
alkalmazott.append(Alkalmazottak("Palacsinta",1997,550,"Igazgató-helyettes"))
alkalmazott.append(Alkalmazottak("Oláh '2-es Golf' Gusztáv",1996,600,"Igazgató"))

"""osszes = fuggvenyek.feladat1(alkalmazott)
print(f"A csapat teljes fizetése: {osszes} fabatka")
fuggvenyek.feladat2(alkalmazott)
beosztottak = fuggvenyek.feladat3(alkalmazott)
print(f"Beosztottak száma: {beosztottak}")
"""
min_index = fuggvenyek.feladat4(alkalmazott)

print(f"A legkevesebb fizetést {alkalmazott[min_index].nev} kapja, ami: {alkalmazott[min_index].fizetes} fabatka")

alkalmazott[min_index].fizetes_emeles(0.2)
