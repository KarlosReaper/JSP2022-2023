import datetime
import fileinput
import sys
import SzyfrCezara
from datetime import date
import os

klucz = int(input("Podaj wartosc liczbowa do szyfrowania (1-10): "))
lokalizacja = input("Podaj lokalizacje do zapisania - jesli w folderze roboczym to nic nie wpisuj: ")
x = str(date.today())
if lokalizacja == '':
    my_absolute_path2 = r'Lista8\plik_zaszyfrowany'+str(klucz)+'_'+x+'.txt'
else:
    if os.path.isdir(lokalizacja) == 0:
        os.makedirs(lokalizacja)
        print('Utworzono wskazana lokalizacje')
    else:
        print('Wskazana lokalizacja juz istnieje')
    my_absolute_path2 = r''+lokalizacja+'\plik_zaszyfrowany'+str(klucz)+'_'+x+'.txt'
my_absolute_path = r'C:\Users\laptop\Desktop\Jezyki skryptowe - python\GitHub\Lista8\plik_do_szyfrowania.txt'

try:
    ff = open(my_absolute_path2,'w')
    with open(my_absolute_path, 'r') as plik: # otworzenie pliku do odczytu
        with open(my_absolute_path2,'w') as ff:
            while 1: # nieskonczony while
                    pobranie = plik.readline() # czytanie pliku po linii
                    if not pobranie: # zakoncz petle jezeli nie ma juz lini w pliku
                        break 
                    else:
                        a = SzyfrCezara.szyfruj(pobranie, klucz)
                        ff.write(a) 
except FileNotFoundError:
    print(f"Nie ma pliku: {'plik_do_szyfrowania.txt'}")
except Exception as wyjatek:
    print(f"Wystąpił błąd: {wyjatek}")