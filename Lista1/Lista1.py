from ast import arg
import math

#
# Zadanie 1
#
print('Zadanie 1')
a    = input('Podaj pierwsza liczbe ')
b    = input('Podaj druga liczbe ')
suma = a+b
print('Suma pierwszej i drugiej liczby to: ',suma)

# Wynik jest złączeniem dwóch liczb, gdyż input uznaje tylko zmienne typu String. 
# Rozwiązaniem może być zmiana typu zmiennej a i b np:

#c     = int(input('Podaj pierwsza liczbe '))
#d     = int(input('Podaj druga liczbe '))
#suma2 = c+d
#print('Suma pierwszej i drugiej liczby po zmianie typu to: ',suma2)

# 
# Zadanie 2
#
print('Zadanie 2')
a    = 3
b    = 4
alfa = math.radians(47)
pole = a*b*math.sin(alfa)/2
print('Pole trojkata to: ',pole)
# Konieczne do tego zadanie było załadowanie pakietu math, który pozwolił zamienić stopnie na radiany oraz
# obliczenie wartości sinusa. 

#
# Zadanie 3
#
print('Zadanie 3')
a    = int(input('Podaj dlugosc pierwszego boku: '))
b    = int(input('Podaj dlugosc drugiego boku: '))
alfa = math.radians(int(input('Podaj kat miedzy bokami w stopniach: ')))
pole = a*b*math.sin(alfa)/2
print('Pole trojkata to: ',pole)
# Aby otrzymać poprawne wartości, konieczne jest zmienienie typu zmiennych a i b ze String na Integer (lub Real)

#
# Zadanie 4
#
print('Zadanie 4')
import builtins
print('Funkcje to: ', dir(__builtins__))
help(print)

print('tekst to: ','" Ala ma kota".')
print('Wynik 2+2 to: ',2+2)
print('Wyniki dzialan (tabulacja) to: ', 2**5, 35//2, 35/2, 35%2, sep='\t')
print('Wyniki dzialan (nowe linie) to: ', 2**5, 35//2, 35/2, 35%2, sep='\n')
# Funkcja dir pozwala na wypisanie listy ze wszystkimi funkcjami dostępnymi w pakiecie
# Klucz sep w print pozawala na wybranie sposobu oddzielania zmiennych.
# \t wstawia większe odstępy; \n rozdziela zmienne przenosząc je do nowych linii

#
# Zadanie 5
#
print('Zadanie 5')
print('Wynik dzialania 5//2 to: ',5//2)
# Działanie to zlicza ile pełnych razy dzielnik zmieści się w dzielnej
print('Wynik zaokraglania round, dzialania 5/2 to: ', round(5/2,1))
# W przypadku funkcji round możemy podać jako drugi argument, 
# numer miejsca po przecinku do którego następuje zaogrąglenie (zgodnie z zasadami matematyki)
print('Wynik zaokraglania floor, dzialania 5/2 to: ', math.floor(5/2))
# Funkcja floor podaje najbliższą wynikowi liczbę całkowitą ale nie większą od samego wyniku

#
# Zadanie 6
#
print('Zadanie 6')
import cmath
print('Wartosc pierwiastka kwadratowego z -17 to: ', cmath.sqrt(-17))
# Konieczne jest użycie pakietu cmath, który pozwala za liczenie pierwiastka z liczby ujemnej (zwraca liczby zespolone)
# W tym przypadku wynikiem jest sama liczba zespolona dlatego wynik jest z dopiskiem j

#
# Zadanie 7
#
print('Zadanie 7')
# Symbol (_) maa specjalne znaczenie, znak podkreślenia zwraca w trybie interaktywnym wartość ostatniego obliczonego wyrażenia
print('Obliczanie wartosci 13*2.1 ', 13*2.1)
#13*2.1
#print('Wartosc _*4 to: ', _*4)
# Trzeba uruchomic w konsoli dwie powyższe linie po usunięciu symboli #

#
# Zadanie 8
#
print('Zadanie 8')
a = int(input('Podaj pierwsza liczbe (wieksza [a]): '))
b = int(input('Podaj druga liczbe (mniejsza [b]): '))
z = a%b
print('Reszta z dzielania a/b to: ', z)
z *= z+3
print('Iloczyn z i z+3 to: ', z)
# zapis z *= z+3 pozwala na przemnożenie z przez liczbe z+3

#
# Zadanie 9
#
print('Zadanie 9')
z = complex(input("Liczba zespolona w postaci a+bj: "))
print('Liczba zespolona to: ', z)
print('|z| = ', abs(z))
print('Arg(z) = ', cmath.phase(z))
print('z* = ', z.conjugate())
# Arg(z) jest równoważne fazie liczby zespolonej (phase)

#
# Zadanie 10
#
print('Zadanie 10')
z = 0+1j
c = cmath.sin(z)
d = cmath.cos(z)
print('Czesc rzeczywista pierwszej liczby: ', c.real, 'Czesc urojona pierwszej liczby: ', c.imag)
print('Czesc rzeczywista drugiej liczby: ', d.real, 'Czesc urojona drugiej liczby: ', d.imag)
suma = c**2+d**2
print('Suma sin^2(z)+cos^2(z)= ', suma)
# Wartość nie jest dokładnie równa 1 ale może to być kwestia numeryczna