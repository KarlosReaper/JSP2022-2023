from ast import arg
import math
import colorsys

#
# Zadanie 6
#
print('Zadanie 6')

R = float(input("Podaj wartosc dla koloru czerwonego (R [0,1]): "))
G = float(input("Podaj wartosc dla koloru zielonego (G [0,1]): "))
B = float(input("Podaj wartosc dla koloru niebieskiego (B [0,1]): "))

# Do zamiany wykorzystuje gotową funkcję z biblioteki colorsys
(H,S,V) = colorsys.rgb_to_hsv(R,G,B)
print("Wartosci HSV to: ", H, S, V)