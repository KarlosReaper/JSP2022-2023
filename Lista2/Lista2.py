#
# Zadanie 1
#
print('Zadanie 1')
print(20*(str(1.2e+3+34.5) +"; "))
# zamieniając wynik działania na ciąg znaków i dodając do niego kolejny ciąg znaków (; ) tworzę nową zmienną typu string.
# Mnożąc ją przez 20 w funkcji print, następuje 20-krotne wypisanie tej zmiennej

#
# Zadanie 2
#
print('Zadanie 2')
tekst = input('Wpisz ciąg znaków: ')
print (30*(tekst+"\n"))
# Podobnie jak w poprzednim zadaniu. W tym przypadku konieczne jest zastosowanie rozdzielenia linii w print (\n)

#
# Zadanie 3
#
print('Zadanie 3')
napis = input('Podaj wyraz: ')
print('Zlaczenie 2 pierwszych i ostatnich liter to: ', napis[0:2]+napis[-2:])
# Wycinanie fragmentu napisu można wykonać za pomoca nawiasu [a:b], gdzie a to pierwsza pozycja do wybrania w wyrazie. 
# Natomiast b to pozycja końca wybranego fragmentu. W przypadku braku liczb przed lub po znaku : to brana jest cała wcześniejsza
# lub dalsza część wyrazu

#
# Zadanie 4
#
print('Zadanie 4')
napis        = input('Podaj napis do zamiany liter: ')
litera       = input('Podaj litere do zamiany: ')
litera2      = input('Podaj litere do wstawienia: ')
poz1         = napis.index(litera)
napis2       = napis.replace(litera, litera2)
print('Zmieniony napis to: ',napis[0:poz1+1]+napis2[poz1+1:])

#
# Zadanie 5
#
print('Zadanie 5')
wyraz1  = input('Podaj pierwszy wyraz do polaczenia: ')
wyraz2  = input('Podaj drugi wyraz do polaczenia: ')
dlugosc = len(wyraz1)
czesc1  = wyraz1[0:dlugosc//2]
czesc2  = wyraz1[dlugosc//2:]
print(czesc1+wyraz2+czesc2)
# Najpierw znajduje środek pierwszego wyrazu i tworze nowe zmienne: znaki przed połową i za połową. 
# Następnie łącze te dwie zmienne dodając w środek jeszcze wyraz do wstawienia

#
# Zadanie 6
#
print('Zadanie 6')
lista = ['Kasia', 'Basia', 'Marek', 'Darek']
print('Stworzona lista to: ', lista)
lista.append('Józek')
print('Rozszerzona lista to: ', lista)
lista.extend(['Ania','Basia'])
print('Ponownie rozszerzona lista to: ', lista)
lista.sort()
print('Posortowana alfabetycznie lista to: ', lista)
print('Czwarty student to: ', lista[3])
print('Dwoch pierwszych studentow to: ', lista[0:2])
print('Dwoch ostatnich studentow to: ', lista[-2:])
while 'Basia' in lista: lista.remove('Basia')
# Aby usunąć wszystkie wystąpienia słowa 'Basia' trzeba stworzyć pętle
print('Lista po usunięciu każdej Basi to : ', lista)
print('Ilosc osob na liscie to: ', len(lista))
krotka = tuple(lista)
print('Utworzona krotka to: ', krotka)
# Listy są strukturą pozwalającą na przechowywanie elementów w sposób uporządkowany
# Krotki, tak jak listy, pozwalają na przechowywanie elementów w sposób uporządkowany. Od list różnią się jednym: 
# po utworzeniu krotki nie możemy modyfikować jej zawartości w trakcie działania aplikacji.

#
# Zadanie 7
#
print('Zadanie 7')
from operator import itemgetter
lista = [(2, 8), (5, 5), (9, 3), (1, 0), (3, 2), (6, 4), (1, 9), (10, 3), (2, 3), (1, 7)]
print('Utworzona lista to: ', lista)
print('Normalnie posortowana lista to: ', sorted(lista))
b = sorted(lista, key=itemgetter(1))
print('Posortowana lista po drugim elemencie to: ', b)
# Konieczne było zastosowanie pakietu operator, który pozwolił na odwołanie się do drugiego elementu w elementach listy

#
# Zadanie 8
#
print('Zadanie 8')
lista = ['a','b','c','d','1','2','3']
wyraz = "".join(lista)
print('Stworzona lista to: ', lista)
print('Stworzony napis to: ', wyraz)
# Funkcja join pozwala na łączenie elementów listy w jeden ciąg znaków. W miejscu " " można wpisać dowolny 
# symbol/wyraz oddzielający kolejne znaki

#
# Zadanie 9
#
print('Zadanie 9')
from itertools import chain
lista = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
print('Wybrana lista to: ', lista)
lista2 = list(chain.from_iterable(lista))
print('Uproszczona lista to: ', lista2)
# Funkcja chain pozwala na rozbicie elementów listy na pojedyncze składowe

#
# Zadanie 10
#
print('Zadanie 10')
war = [*range(3,100,3)]
print('Lista wielokrotnosci liczby 3 to: ', war)
del war[4::3]
print('Lista wielokrotnosci liczby 3 po usunieciu co 3 elementu to: ', war)
suma = sum(war)
print('Suma elementow listy to: ', suma)
srednia = suma/len(war)
print('Srednia arytmentyczna z elementow listy to: ', srednia)
# Symbol * przed range rozpisuje elementy na pojeduncze. Inaczej wynik to po prostu range(3,100,3)
# Funkcja del pozwala na usunięcie wybranych elementów listy, oraz na wybór kroku do usuwania: del lista[start,end,step]
# Funkcja sum oblicza sumę liczb w liście