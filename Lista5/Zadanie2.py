from ast import arg
import math

#
# Zadanie 2
#
print('Zadanie 2')

liczban = int(input('Podaj w postaci dziesietnej liczbe od 1 do 1999: '))




# dodaj jeszcze pelne dziesiatki bo brakuje!!!!!!!!!!

def liczby(liczban):

  # Tworze liste z nazwali liczby od 1 do 59 (dla pewnosci pomijam polskie znaki)

  liczbys1 = ['jeden', 'dwa', 'trzy', 'cztery', 'piec', 'szesc', 'siedem', 'osiem', 'dziewiec', 'dziesiec']
  liczbys2 = ['jedenascie', 'dwanascie', 'trzynascie' ,'czternascie', 'pietnascie', 'szesnascie', 'siedemnascie', 'osiemnascie', 'dziewietnascie']
  liczbys3 = ['dwadziescia','trzydziesci','czterdziesci','piecdziesiat','szescdziesiat','siedemdziesiat','osiemdziesiat','dziewiecdziesiat']
  liczbys4 = ['sto','dwiescie','trzysta','czterysta','piecset','szescset','siedemset','osiemset','dziewiecset']
  liczbys = liczbys1+liczbys2
  for i in range(8):
    c = liczbys3[i]
    liczbys = liczbys+[c]
    for j in range(9):
        c = liczbys3[i]+' '+liczbys1[j]
        liczbys = liczbys+[c]
  for i in range(9):
    liczbys = liczbys+[liczbys4[i]]
    for j in range(10):
      c = liczbys4[i]+' '+liczbys1[j]
      liczbys = liczbys+[c]
    for j in range(9):
      c = liczbys4[i]+' '+liczbys2[j]
      liczbys = liczbys+[c]
    for j in range(8):
      c = liczbys4[i]+' '+liczbys3[j]
      liczbys = liczbys+[c]
      for k in range(9):
        c = liczbys4[i]+' '+liczbys3[j]+' '+liczbys1[k]
        liczbys = liczbys+[c]
    
  liczbys = liczbys+['tysiac']
  for j in range(10):
    c = 'tysiac '+liczbys1[j]
    liczbys = liczbys+[c]
  for j in range(9):
    c = 'tysiac '+liczbys2[j]
    liczbys = liczbys+[c]
  for j in range(8):
    c = 'tysiac '+liczbys3[j]
    liczbys = liczbys+[c]
    for k in range(9):
      c = 'tysiac '+liczbys3[j]+' '+liczbys1[k]
      liczbys = liczbys+[c]
    

  for i in range(9):
    c = 'tysiac '+liczbys4[i]
    liczbys = liczbys+[c]
    for j in range(10):
      c = 'tysiac '+liczbys4[i]+' '+liczbys1[j]
      liczbys = liczbys+[c]
    for j in range(9):
      c = 'tysiac '+liczbys4[i]+' '+liczbys2[j]
      liczbys = liczbys+[c]
    for j in range(8):
      c = 'tysiac '+liczbys4[i]+' '+liczbys3[j]
      liczbys = liczbys+[c]
      for k in range(9):
        c = 'tysiac '+liczbys4[i]+' '+liczbys3[j]+' '+liczbys1[k]
        liczbys = liczbys+[c]
 
 # Sprawdzam czy podany ciag znakow jest na liscie
  if liczban > -1 and liczban < 1999:
    print("Podana liczba to: ",liczbys[liczban])
  else:
    print("Podano bledna liczbe")
  

liczby(liczban-1)