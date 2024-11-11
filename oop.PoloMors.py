class Suns():

    def __init__(self, vards):
        self.vards = vards
    
    def balss(self):
        return self.vards + " saka vau!"
    
class Kakis:
    def __init__(self, vards):
        self.vards = vards
    def balss(self):
        return self.vards + " saka ņau!"
    
niko = Suns("Niko")
felikss = Kakis("Felikss")

print(niko.balss())
print(felikss.balss())

for pet in [niko, felikss]:
    print(type(pet))
    print(type(pet.balss()))

def pet_balss(pet):
    print(pet.balss())

pet_balss(niko)
pet_balss(felikss)
