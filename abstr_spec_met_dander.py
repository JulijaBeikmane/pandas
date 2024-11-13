mans_list = [1, 2, 3]

print(len(mans_list))


class Piemers():
    pass 

paraugs = Piemers()
print(paraugs)

print(mans_list)

class Gramata: 
    def __init__(self, nosaukums, autors, lpp):

        self.nosaukums = nosaukums
        self.autors = autors
        self.lpp = lpp

    def __str__(self):
        return f"Grāmatas {self.nosaukums} autors ir {self.autors}"
    
    def __len__(self):
        return self.lpp
    
    def __del__(self):
        print("Grāmata ir izdzēsta")
    
gr = Gramata("Zelta zirgs", "Rainis", 200)
print(gr)
print(len(gr))

# del gr
# print(gr)
