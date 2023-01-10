
#
# Zadanie 3
#

from ast import IsNot


print('Zadanie 3')

class podlisty3:
    def __init__(self,lista):
        dlugosc = len(lista)
        if dlugosc < 3:
            self.wynik = 'Zbyt malo elementow'
        elif dlugosc == 3:
            suma = lista[0]+lista[1]+lista[2]
            if suma == 0:
                self.wynik = lista
            else:
                self.wynik = 'Brak podlist o sumie rownej 0'
        else:
            listy = []
            for i in range(dlugosc-2):
                for j in range(dlugosc-i-1):
                    for k in range(dlugosc-j-i-2):
                        elem1 = lista[i]
                        elem2 = lista[j+i+1]
                        elem3 = lista[k+j+i+2]
                        suma = elem1+elem2+elem3
                        if suma == 0:
                            listy.append([elem1,elem2,elem3])

            if len(listy) == 0:
                self.wynik = 'Brak podlist o sumie rownej 0'
            else:
                self.wynik = listy



lista = [1,-2,2,3,0,-3,-1] # Deklaracja listy to sprawdzenia
k = podlisty3(lista) # przypisuje do k klase z podstawiona lista
print(k.wynik)