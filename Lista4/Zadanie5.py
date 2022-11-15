from ast import arg
import math
import itertools

#
# Zadanie 5
#
print('Zadanie 5')

try:
    lista = []
      
    while True:
        lista.append(int(input("Podaj kolejny element listy (Przerwanie w momencie wpisania znaku innego jak cyfra) ")))
          
# jesli podany element nie jest liczba to przerywa tworzenie listy
except:
    print("Utworzona lista to: ",lista)

permutacje = list(itertools.permutations(lista))
print("Permutacje to: ",permutacje)