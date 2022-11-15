from ast import arg
import math

#
# Zadanie 8
#
print('Zadanie 8')

# Definiuję funkcję do szeregu harmonicznego
def szereg(n):
    suma=0
    for i in range(n):
        suma = suma+1/(i+1)
    print("Suma szeregu to: ", suma)
    return suma

# Wczytanie liczby wierszy
n = int(input("Podaj liczbe elementow szeregu harmonicznego: "))
szereg(n)