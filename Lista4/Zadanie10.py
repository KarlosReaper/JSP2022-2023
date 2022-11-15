from ast import arg
import math

#
# Zadanie 10
#
print('Zadanie 10')

# Definiuję funkcję do znajdowania największego wspólnego dzielnika
def nwd(a, b):
    while b: # do czasu gdy b = 0, wtedy pozostałe 'a' jest największym dzielnikiem
        # pod a podstawiam b, natomiast pod b reszte z dzielenia a i b
        a, b = b, a%b
    return a

a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))
print("Najwiekszy wspolny dzielnik to: ",nwd(a,b))