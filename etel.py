class Etel:
    def __init__(self,nev:str="",ar:int=1000):
        self.nev = nev
        self.ar = ar
        self.allapot = "Folyamatban"

    def keszul(self):
        self.allapot = "kész"

    def __str__(self):
        return f"Étel neve: {self.nev}, Ár: {self.ar} Ft, Állapot: {self.allapot}"
