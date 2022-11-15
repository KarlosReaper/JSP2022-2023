from ast import arg
import math

#
# Zadanie 9
#
print('Zadanie 9')

# Definiuję funkcję do silni (można też użyć po prostu funkcji factorial)
def silnia(n):
    iloczyn=1
    for i in range(n):
        iloczyn = iloczyn*(i+1)
    print("Silnia to: ", iloczyn)
    return iloczyn

# Wczytanie liczby wierszy
n = int(input("Podaj liczbe do obliczenia silni: "))
silnia(n)