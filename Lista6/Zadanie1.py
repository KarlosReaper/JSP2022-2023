import trojkat
import math

#
# Zadanie 1
#

print('Zadanie 1')

a = int(input("Podaj dlugosc pierwszego boku trojkata: "))
b = int(input("Podaj dlugosc drugiego boku trojkata: "))
c = int(input("Podaj dlugosc trzeciego boku trojkata: "))

sprt = trojkat.spr(a,b,c)

if sprt == 1:
    print("Obwod trojkata to: ", trojkat.obwod(a,b,c))
    print("Pole trojkata to: ", trojkat.pole(a,b,c))
    print("Trojkat jest: ", trojkat.rodzaj(a,b,c))
    print("Trojkat jest: ", trojkat.kat(a,b,c))
else:
    print('Trojkat nie istnieje')