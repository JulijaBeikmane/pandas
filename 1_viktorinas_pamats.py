class QuizBrain:
    def __init__(self, jaut_saraksts): 
        self.jaut_saraksts = jaut_saraksts
        self.jaut_nr = 0
        punkti = 0

    def vel_ir_jautajumi(self):
        return self.jaut_nr < len(self.jaut_saraksts)


    def nakamais_jaut(self):
       
        pasreiz_jaut = self.jaut_saraksts[self.jaut_nr] 
        self.jaut_nr += 1 
        lietotaja_atb = input(f"{self.jaut_nr}.jautājums: {pasreiz_jaut.teksts} (Patiesi/Aplami): ")
        self.parbaudi_atbildi(lietotaja_atb, pasreiz_jaut.atbilde)

    def parbaudi_atbildi(self, lietotaja_atb, pareiza_atbilde):
        if lietotaja_atb.lower() == pareiza_atbilde.lower():
            self.punkti += 1
            print("Pareizi!")
        else:
            print("Kļūda!")
        if lietotaja_atb.lower() == pareiza_atbilde.lower():
            print("Pareizi!")
        else:
            print("Kļūda!")
            print(f"Pareizā atbilde ir {pareiza_atbilde}.")
            print(f"Pareizā atbilde ir {pareiza_atbilde}.")
            print(f"Tev ir {self.punkti} no {self.jaut_nr} punktiem.")
            print("\n")


    
