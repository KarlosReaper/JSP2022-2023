import math
import time
import random

#
# Zadanie 2
#

print('Zadanie 2')

def sortuj_wstaw(tab, n): #tworzymy metode do sortowania poprzez wstawianie
    for x in range(1, n):
        selected = tab[x]  #aktualnie wybrany element
        y = x-1 #przygotowujemy iteracje poprzez pozostale elementy
        while y >= 0 and selected < tab[y]: #dopoki nie znajdziemy elementu mniejszego od wybranego i nie natrafimy na poczatek tablicy
            tab[y+1] = tab[y] #zamieniamy elementy miejscami
            y -= 1 #modyfikujemy zmienna iteracyjna
        tab[y+1] = selected #po znalezieniu mniejszego elementu, zamieniamy go z wybranym
    print(tab)

tab1 = []
tab2 = []
tab3 = []
for i in range(99):
    tab1.append(random.randint(0,20))
for i in range(199):
    tab2.append(random.randint(0,20))
for i in range(299):
    tab3.append(random.randint(0,20))
n1 = len(tab1)
n2 = len(tab2)
n3 = len(tab3)

t1 = time.time()
print(tab1)
print(" ")
sortuj_wstaw(tab1,n1)
print(" ")
t2 = time.time()
print(tab2)
print(" ")
sortuj_wstaw(tab2,n2)
print(" ")
t3 = time.time()
print(tab1)
print(" ")
sortuj_wstaw(tab3,n3)
print(" ")
t4 = time.time()
print("Czas 100 to: ", t2-t1)
print("Czas 200 to: ", t3-t2)
print("Czas 300 to: ", t4-t3)
print("Czas nie rosnie liniowo!")