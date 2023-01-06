import math
import numpy
import os.path
import sys


#
# Zadanie 2
#
print('Zadanie 2')

# Wczytuje dane
input_data = sys.argv[1]
if os.path.isfile(input_data):
    with open(input_data, 'r') as plik:
        dane = plik.read()
        dane = dane.strip().split(',')
        print('Dane z pliku to: ', dane)
        dane = list(map(int, dane))
else:
    dane = sys.argv[1].split(',')
    dane = list(map(int, dane))

srednia = numpy.sum(dane)/len(dane)
wariancja = numpy.sum( (dane - srednia)**2 ) / len(dane)
odchylenie = numpy.sqrt(wariancja)
print('Parametry to: ', end='\n')
print('srednia arytmetyczna = ',srednia, end='\n')
print('wariancja = ',wariancja, end='\n')
print('odchylenie standardowe = ',odchylenie, end='\n')
