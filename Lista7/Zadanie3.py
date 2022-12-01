import math
import time
import random

#
# Zadanie 3
#

print('Zadanie 3')


def sortowanie_babelkowe(lista):
    n = len(lista) # Sprawdza liczbe elementow
    
    # powtarza dopoki n > 1
    while n > 1:
        zamien = False
        for l in range(0, n-1):
            if lista[l] > lista[l+1]: # porownuje sasiednie liczby
                lista[l], lista[l+1] = lista[l+1], lista[l]
                zamien = True
                
        n -= 1 # zmniejsza n o 1
        if zamien == False: break # przerywa jesli liczba nie zostala przestawiona
        
    return lista
        

tab1 = []
tab2 = []
tab3 = []
for i in range(99):
    tab1.append(random.randint(0,20))
for i in range(199):
    tab2.append(random.randint(0,20))
for i in range(299):
    tab3.append(random.randint(0,20))

t1 = time.time()
print(tab1)
print(" ")
a = sortowanie_babelkowe(tab1)
print(a)
print(" ")
t2 = time.time()
print(tab2)
print(" ")
b = sortowanie_babelkowe(tab2)
print(b)
print(" ")
t3 = time.time()
print(tab1)
print(" ")
c = sortowanie_babelkowe(tab3)
print(c)
print(" ")
t4 = time.time()
print("Czas 100 to: ", t2-t1)
print("Czas 200 to: ", t3-t2)
print("Czas 300 to: ", t4-t3)
print("Czas nie rosnie liniowo! Dluzsza metoda niz w zadaniu 2.")