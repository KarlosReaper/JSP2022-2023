from ast import arg
import math

#
# Zadanie 4
#
print('Zadanie 4')

# Definiuję funkcję obliczającą wartość elementu w ciągu (a i q mają początkowe wartości)
def ciag(n,a=1,q=2):
    an = a*q**(n-1)
    print("Wartosc wyrazu to: ",an)
    return an

# Wczytuje numer elementu i sprawdzam czy użytkownik chce podać pierwszy element ciągu i jego iloraz
n = int(input("Podaj numer elementu (n > 0): "))
decyzja1 = input("Czy chcesz podac pierwszy element? (tak/[nie - dowolny inny znak/ciag znakow]): ")
decyzja2 = input("Czy chcesz podac iloraz ciagu? (tak/[nie - dowolny inny znak/ciag znakow]): ")

# Sprawdzam podane przez użytkownika decyzje i obliczam odpowiednio wartość elementu ciągu
if decyzja1 == "tak":
    a1 = float(input("Podaj wartosc pierwszego elementu: "))
    if decyzja2 == "tak":
        q1 = float(input("Podaj wartosc ilorazu ciagu: "))
        ciag(n,a=a1,q=q1)
    else:
        ciag(n,a=a1)
else:
    if decyzja2 == "tak":
        q1 = float(input("Podaj wartosc ilorazu ciagu: "))
        ciag(n,q=q1)
    else:
        ciag(n)
