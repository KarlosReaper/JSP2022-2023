from ast import arg
import math

#
# Zadanie 1
#
print('Zadanie 1')

liczbas = input('Podaj slownie liczbe od 1 do 59 (bez polskich znakow): ')

def slownie(liczbas):

  # Tworze liste z nazwali liczby od 1 do 59 (dla pewnosci pomijam polskie znaki)
  liczbys1 = ['jeden', 'dwa', 'trzy', 'cztery', 'piec', 'szesc', 'siedem', 'osiem', 'dziewiec', 'dziesiec']
  liczbys2 = ['jedenascie', 'dwanascie', 'trzynascie' ,'czternascie', 'pietnascie', 'szesnascie', 'siedemnascie', 'osiemnascie', 'dziewietnascie', 'dwadziescia']
  liczbys3 = ['dwadziescia jeden','dwadziescia dwa','dwadziescia trzy','dwadziescia cztery','dwadziescia piec','dwadziescia szesc','dwadzeiscia siedem','dwadziescia osiem','dwadziescia dziewiec','trzydziesci']
  liczbys4 = ['trzydziesci jeden','trzydziesci dwa','trzydziesci trzy','trzydziesci cztery','trzydziesci piec','trzydziesci szesc','trzydziesci siedem','trzydziesci osiem','trzydziesci dziewiec','czterdziesci']
  liczbys5 = ['czterdziesci jeden','czterdziesci dwa','czterdziesci trzy','czterdziesci cztery','czterdziesci piec','czterdziesci szesc','czterdziesci siedem','czterdziesci osiem','czterdziesci dziewiec','piecdziesiat']
  liczbys6 = ['piecdziesiat jeden','piecdziesiat dwa','piecdziesiat trzy','piecdziesiat cztery','piecdziesiat piec','piecdziesiat szesc','piecdziesiat siedem','piecdziesiat osiem','piecdziesiat dziewiec']
  liczbys = liczbys1+liczbys2+liczbys3+liczbys4+liczbys5+liczbys6
  
  # Sprawdzam czy podany ciag znakow jest na liscie
  if liczbas in liczbys:
    print(liczbys.index(liczbas)+1)
  else:
    print("Podano bledna liczbe")

slownie(liczbas)
for i in range(10):
    print(i)