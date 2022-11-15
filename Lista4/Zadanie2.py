from ast import arg
import math

#
# Zadanie 2
#
print('Zadanie 2')
lista = [4,4,4,1,1,1,2,2,3]

# definiuję funkcję
def powtorzenia(lista):
    lista2 = set(lista)    

print(lista)
print(powtorzenia(lista))

# funkcja set zmienia listę w zbiór bez powtarzających się elementów i porządkuje ją od najmniejszej do największej liczby