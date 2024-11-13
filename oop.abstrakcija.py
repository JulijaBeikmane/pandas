#abstrakcija - abstraktas klases mantošan, pašu klasi neizmanto. Pašu abstrakto klasi nav paredzēts instanciēt (nav paredzēts no tās veidot objektus), Tā ir paredzēta, lai kalpotu kā bāzes klase.

class Dzivnieks:
    def __init__(self, vards):
        self.vards = vards 
    #nav predzēts, ka šī klase tiks instanciēta
    def balss(self):
        raise NotImplementedError("Šai abstraktajai klasei jābūt implementētai(realizētai/īstenotai) apakšklasē")
    
mans_dzivnieks = Dzivnieks("Fredis")

#izraisa kļūdu
# mans_dzivnieks.balss()

class Suns(Dzivnieks):
    def balss(self):
        return f"{self.vards} saka vau!"
    
niko = Suns("Niko")
print(niko.balss())
    
