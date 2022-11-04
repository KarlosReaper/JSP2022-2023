from ast import arg
import math

#
# Zadanie 2
#
print('Zadanie 2a')
liczba = int(input('Podaj liczbe '))
odp = ("Liczba jest parzysta", "Liczba jest nieparzysta")
if liczba%2 == 0:  # sprawdzam czy reszta z dzielenia przez 2 jest rowna 0
    print('Liczba jest parzysta')
elif liczba%2 == 1: # sprawdzam czy reszta z dzielenia przez 2 jest rowna 0
    print('Liczba jest nieparzysta')

print('Zadanie 2b')
# reszta z dzielenia moze byc rowna 0 albo 1 a wiec tworze tablice z 2 wartosciami, jesli reszta jest 0 to wypisuje pierwszy element
liczba = int(input('Podaj liczbe '))
odp = ("Liczba jest parzysta", "Liczba jest nieparzysta")
print(odp[liczba%2])