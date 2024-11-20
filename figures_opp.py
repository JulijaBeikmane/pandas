import math
class Cilindrs:


    def __init__(self, augstums=1, radius=1):
        self.augstums = augstums
        self.radius = radius


    def tilpums(self):
        # def __init__(self):
        #     Cilindrs.__init__(self)
        return math.pi * self.radius ** 2 * self.augstums
            


    def virsmas_laukums(self):
      return 2 * math.pi * self.radius ** 2 + 2 * math.pi * self.radius * self.augstums




# REZULTĀTA PEMĒRS
c = Cilindrs(2, 3)
print("Cilindra tilpums:", c.tilpums())  
print("Cilindra virsmas laukums:", c.virsmas_laukums())  

# 2.uzdvums


class Line:


    def __init__(self, koor1, koor2):
        self.koor1 = koor1
        self.koor2 = koor2


    def attalums(self):

        return math.sqrt((self.koor2(0) - self.koor1(0)) + (self.koor2(1) - self.koor1(1)))


    def virziens(self):
        return (self.koor2[1] - self.koor1[1]) / (self.koor2[0] - self.koor1[0])



# REZULTĀTA PEMĒRS


koordinata1 = (3,2)

koordinata2 = (8,10)


li = Line(koordinata1,koordinata2)


li.attalums()

li.virziens()
