def summa(a, b):
    return a+b

def atnemsana(a, b):
    return a-b

def dalisana(a, b):
    return a/b

def reizinasana(a, b):
    return a*b

print(summa(2, 6))
print(atnemsana(2, 6))
print(dalisana(2, 6))
print(reizinasana(2, 6))

#pirmās klases objekti var tikt padoti kā argumenti
def kalkulators(sk1, sk2, operat):
    return operat(sk1, sk2)

print(kalkulators(2, 6, reizinasana))
print(kalkulators(2, 6, dalisana))
print(kalkulators(12, 8, atnemsana))

rezult = kalkulators(1.5, 5.9, reizinasana)
print(rezult)

#Nested funkctions(funkcija funkcijā)
#l = [1, 8, [2,5,6], 59]

def areja_funkcija():
    print("Es esmu ārējā funkcija")

    def iekseja_funkcija():
        print("Es esmu iekšējā funkcija")

    return iekseja_funkcija

ieks_fja = areja_funkcija()
ieks_fja()

#Python decorators 
import time

def decorator_function(function):

    def wrapper_function():
        function()
    return wrapper_function
#Izveido vienkāršu funkciju 
def sveiki():
    # pieliek aizturi
    time.sleep(2)
    print("Sveiki!")

sveiki()


#Kā uzlikt aizkavi visām funkcijām
def aizkave_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()

    return wrapper_function

@aizkave_decorator

def labrit():
    print("Labrīt")

@aizkave_decorator

def labdien():
    print("Labdien!")

@aizkave_decorator

def labvakar():
    print("Labvakar!")

labrit()
labdien()
labvakar()
