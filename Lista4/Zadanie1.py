from ast import arg
import math

#
# Zadanie 1
#
print('Zadanie 1')

# Wczytanie liczb do listy
try:
    lista = []
      
    while True:
        lista.append(int(input("Podaj kolejny element listy (Przerwanie w momencie wpisania znaku innego jak cyfra) ")))
          
# jesli podany element nie jest liczba to przerywa tworzenie listy
except:
    print(lista)

dlugosc = len(lista)
suma = 0
iloczyn = 0
decyzja = input("wpisz litery: 's' do liczenia sumy, 'i' do liczenia iloczynu oraz 'si' do obu: ")

if decyzja == 'i' or decyzja == 'si' or decyzja == 's':
    
    for i in range(dlugosc):
        suma = suma+lista[i]
        if i == 0:
            iloczyn = lista[i]
        elif i > 0:
            iloczyn = iloczyn*lista[i]
    
    if decyzja == 's':
        if dlugosc >= 1:
            print("Suma elementow listy to: ", suma)
        else:
            print("Brak elementow w liscie")
    elif decyzja == 'i':
        if dlugosc >= 1:
            print("Iloczyn elementow listy to: ", iloczyn)
        else:
            print("Brak elementow w liscie")
    elif decyzja == 'si':
        if dlugosc >= 1:
            print("Suma elementow listy to: ", suma)
            print("Iloczyn elementow listy to: ", iloczyn)
        else:
            print("Brak elementow w liscie")

elif decyzja != 's' or decyzja != 'i' or decyzja != 'si' and dlugosc > 0:
    print("Bledna decyzja")
elif dlugosc == 0:
    print("Brak elementow")
