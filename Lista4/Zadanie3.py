from ast import arg
import math

#
# Zadanie 3
#
print('Zadanie 3')

#wprowadzam dane
kat = float(input("Podaj wartosc kata do zamiany: "))
rodzaj = input("Podaj typ kata na ktory nalezy zamienic (r - radiany; s - stopnie): ")

# definiuję funkcję do zamiany kątów
def stopnie(kat, rodzaj):
    if rodzaj == 'r':
        kat2 = kat*math.pi/180.0
        print('Wartosc kata po zamianie na radiany to: ', kat2)
        return kat2
    elif rodzaj == 's':
        kat2 = kat*180.0/math.pi
        print('Wartosc kata po zamianie na stopnieto: ', kat2)
        return kat2
    elif rodzaj != 'r' or rodzaj != 's':
        print("podano bledny rodzaj kata (r - radiany; s - stopnie)")

stopnie(kat,rodzaj)