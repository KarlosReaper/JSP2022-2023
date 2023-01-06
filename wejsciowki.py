import math
import time
import random
import sys

#
# Zadanie w ramach wejsciowek
#

print('Zadanie w ramach wejsciowek')

# sortowanie buble
#------------------------------------------------------------------------------
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

# sortowanie merge
#------------------------------------------------------------------------------
def mergeSort(arr):
    if len(arr) > 1:

        # Dziele podana tablice na 2 czesci
        mid = len(arr)//2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]
 
        # Powtarzam to wszystko na kazdej z czesci
        mergeSort(sub_array1)
        mergeSort(sub_array2)
         
        #  Początkowe wartości wskaźników, których używamy do śledzenia miejsca, w którym się znajdujemy w każdej tablicy
        i = j = k = 0
 
        # Dopóki nie dojdziemy do końca początku lub końca, wybieraj większe spośród elementów początkowych i końcowych i 
        # umieszczaj je we właściwej pozycji w posortowanej tablicy
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1
 
        # Kiedy wszystkie elementy zostaną przemieszczone w arr1 lub arr2, umieść pozostałe elementy w posortowanej tablicy
        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1
 
        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1
 

# sortowanie quicksort
#------------------------------------------------------------------------------
def quickSort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quickSort(items_lower) + [pivot] + quickSort(items_greater)
sys.setrecursionlimit(10000)
tab11 = []
tab21 = []
tab31 = []
for i in range(99):
    tab11.append(random.randint(0,100))
for i in range(999):
    tab21.append(random.randint(0,100))
for i in range(1999):
    tab31.append(random.randint(0,100))
tab12 = tab11
tab13 = tab11
tab22 = tab21
tab23 = tab21
tab32 = tab31
tab33 = tab31
size1 = len(tab13)
size2 = len(tab23)
size3 = len(tab33)

t11 = time.time()
#print(" ")
a = sortowanie_babelkowe(tab11)
#print(a)
#print(" ")
t12 = time.time()

t21 = time.time()
#print(" ")
a = sortowanie_babelkowe(tab21)
#print(a)
#print(" ")
t22 = time.time()

t31 = time.time()
#print(" ")
a = sortowanie_babelkowe(tab31)
#print(a)
#print(" ")
t32 = time.time()
print('Babelkowe 100 el: ', t12-t11)
print('Babelkowe 1000 el: ', t22-t21)
print('Babelkowe 2000 el: ', t32-t31)
print(" ")

t13 = time.time()
#print(" ")
mergeSort(tab12)
#print(tab12)
#print(" ")
t14 = time.time()

t23 = time.time()
#print(" ")
mergeSort(tab22)
#print(tab22)
#print(" ")
t24 = time.time()

t33 = time.time()
#print(" ")
mergeSort(tab32)
#print(tab32)
#print(" ")
t34 = time.time()
print('Merge sort 100 el: ', t14-t13)
print('Merge sort 1000 el: ', t24-t23)
print('Merge sort 2000 el: ', t34-t33)
print(" ")



t15 = time.time()
#print(" ")
quickSort(tab13)
#print(tab13)
#print(" ")
t16 = time.time()
t25 = time.time()
#print(" ")
quickSort(tab23)
#print(tab23)
#print(" ")
t26 = time.time()
t35 = time.time()
#print(" ")
quickSort(tab33)
#print(tab33)
#print(" ")
t36 = time.time()
print('Quick sort 100 el: ', t16-t15)
print('Quick sort 1000 el: ', t26-t25)
print('Quick sort 2000 el: ', t36-t35)
print(" ")
print("Merge jest zawsze najszybsze, buble w malych tablicach jest wolniejsze od quick sort ale jest szybsze")
print("Powyzej 2000 elementow jest problem z quick sort (zakladam ze z setrecursionlimit)")