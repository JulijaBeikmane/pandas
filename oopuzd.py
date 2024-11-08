# class Kino:
#     def __init__(self, skatitajs, filma):
#         self.skatitajs = skatitajs
#         self.film = filma
#         self.summa = 0
#     def maksa(self):
#         self.summa += 5
#     def izdruka_maksu(self):
#         print(f"{self.skatitajs} maksā {self.summa}EUR par filmu {self.film} " )

# skatitajs_1 = Kino("Ieva", "Šreks")
# skatitajs_2 = Kino("Jānis", "Straume")

# skatitajs_1.maksa()
# skatitajs_2.maksa()

# skatitajs_1.izdruka_maksu()
# skatitajs_2.izdruka_maksu()



class Kino:
    def __init__(self, skatitajs):
        self.skatitajs = skatitajs
        self.filmas = []
        self.summa = 0
    
    def pievienot_filmu(self, filma):
        self.filmas.append(filma)
        self.summa += 5
    
    def izdruka_maksu(self):
         print(f"{self.skatitajs} kopā par visām filmāmmaksā {self.summa}EUR " )
skatitajs_1 = Kino("Ieva")
skatitajs_1.pievienot_filmu("Šreks")
skatitajs_1.pievienot_filmu("Straume")
skatitajs_1.izdruka_maksu()
