#manošana
class Dzivnieks:

    def __init__(self):
        print("Dzīvnieks ir izveidots")

    def kas_es_esmu(self):
        print("Es esmu dzīvnieks")

    def est(self):
        print("Es ēdu")

class Suns(Dzivnieks):
    def __init__(self):
        Dzivnieks.__init__(self)
        print("Suns ir izveidots")

    def kas_es_esmu(self):
       print("Es esmu suns")

    def balss(self):
        print("Vau!")


mans_dzivnieks = Dzivnieks()

mans_dzivnieks.kas_es_esmu()
mans_dzivnieks.est()

mans_suns = Suns()
mans_suns.est()
mans_suns.kas_es_esmu()
mans_suns.balss()

class Kakis(Dzivnieks):
    def __init__(self):
        Dzivnieks.__init__(self)
        print("Kakis ir izveidots")

    def kas_es_esmu(self):
       print("Es esmu kakis")

    def balss(self):
        print("Mjau!")

mans_dzivnieks = Dzivnieks()

mans_dzivnieks.kas_es_esmu()
mans_dzivnieks.est()

mans_kakis = Kakis()
mans_kakis.kas_es_esmu()
mans_kakis.balss()
