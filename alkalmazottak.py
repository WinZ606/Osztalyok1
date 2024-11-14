class Alkalmazottak:
    def __init__(self,nev:str="",szul_datum:int=2000,fizetes:int=200,pozicio:str=""):
        self.nev = nev
        self.szul_datum = szul_datum
        self.fizetes = fizetes
        self.pozicio = pozicio
        self.kor = 2024 - szul_datum

        def fizetes_emeles(self,szazalek):
            self.fizetes *= (1+szazalek)

    def __str__(self):
        return f"Alkalmazott neve: {self.nev}, születési év: {self.szul_datum}, fizetes: {self.fizetes} fabatka, pozíció: {self.pozicio}, kor: {self.kor} év"
    
