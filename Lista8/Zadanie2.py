import datetime
import fileinput
import sys
import SzyfrCezara
from datetime import date
import os

lokalizacja = input("Podaj lokalizacje do odczytania plikow - jesli w folderze roboczym to nic nie wpisuj: ")

if lokalizacja == '':
    lok2 = r'Lista8'
else:
    lok2 = lokalizacja 

try:
    for f_name in os.listdir(lok2):
        if f_name.startswith('plik_zaszyfrowany'):
            my_absolute_path2 = r''+lok2
            my_absolute_path2=os.path.join(my_absolute_path2, f_name)
            string1 = f_name[17:]
            my_absolute_path = r''+lok2+r'\plik_deszyfrowany'+string1
            if len(f_name) == 33:
                klucz = int(f_name[17:18])
            else:
                klucz = int(f_name[17:19])
            with open(my_absolute_path2, 'r', encoding="utf8") as plik:
                ff = open(my_absolute_path,'w')
                while 1: # nieskonczony while
                    pobranie = plik.readline() # czytanie pliku po linii
                    if not pobranie: # zakoncz petle jezeli nie ma juz lini w pliku
                        break 
                    else:
                        a = SzyfrCezara.deszyfruj(pobranie, klucz)
                        ff.write(a)
                ff.close()
except FileNotFoundError:
    print(f"Nie ma zaszyfrowanych plikow w podanej lokalizacji")
except Exception as wyjatek:
    print(f"Wystąpił błąd: {wyjatek}")