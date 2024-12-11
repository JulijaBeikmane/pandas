#Uzd2
class Akvarijs:
    def __init__(self, platums, garums, augstums):
        self.platums = platums
        self.garums = garums
        self.augstums = augstums
    def tilpums(self):
        print(f"Platums: {self.platums}, Garums: {self.garums}, Augstums: {self.augstums}")
        tilp = self.platums * self.garums * self.augstums
        return (f"Tilpums: {tilp}")
    
akv1 = Akvarijs(7, 8, 10)
akv2 = Akvarijs(15, 13, 4)
print(akv1.tilpums())
akv2.tilpums()
print(akv2.tilpums())
#Uzd3
class Akvarijs:
    def __init__(self, platums, garums, augstums):
        self.__platums = platums
        self.__garums = garums
        self.__augstums = augstums

    def tilpums(self):
        print(f"Platums: {self.platums}, Garums: {self.garums}, Augstums: {self.augstums}")
        tilp = self.platums * self.garums * self.augstums
        return (f"Tilpums: {tilp}")
    @property
    def platums(self):
        return self.__platums
    @property
    def garums(self):
        return self.__garums
    @property
    def augstums(self):
        return self.__augstums
    
    
akv1 = Akvarijs(7, 8, 10)
akv2 = Akvarijs(15, 13, 4)
print(akv1.tilpums())
print(akv2.tilpums())

#Uzd4
class Sportists:
    def __init__(self, terpi, apavi, quantity):
        self.terpi = terpi 
        self.apavi = apavi 
        self.quantity = quantity
    def __str__(self):
        return f"{self.__class__.__name__}, Terpi:{self.terpi}, Apavi:{self.apavi}, Quantity: {self.quantity}" 
    def get_total_price(self):
        total_price = (self.terpi + self.apavi) * self.quantity
        print(f"Terpes izmaksas: {self.terpi}, Apavu izmaksas: {self.apavi}, Total Price: {total_price:.2f}")
        return total_price

sportists1 = Sportists(20, 45, 3)
print(sportists1.get_total_price())
sportists2 = Sportists(17, 60, 7)
print(sportists2.get_total_price())

# #uzd5
class Hokejs(Sportists):
    def __init__(self, terpi, apavi, slidas, nuja, quantity):
         super().__init__(terpi, apavi, quantity)
         self.slidas = slidas 
         self.nuja = nuja
    def __str__(self):
        return super().__str__() + f", Nuja:{self.nuja}, slidas:{self.slidas}"
    def get_total_price(self):
         total_price = (self.terpi + self.apavi + self.nuja + self.slidas) * self.quantity
         return total_price
        
          
        
sportists3 = Hokejs(20, 45, 30, 10, 2)
print(sportists3)
print(sportists3.get_total_price())
sportists4 = Hokejs(60, 10, 54, 5, 4)
print(sportists4)
print(sportists4.get_total_price())
