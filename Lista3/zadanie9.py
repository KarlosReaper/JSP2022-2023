#
# Zadanie 9
#

print('Zadanie 9')
m = int(input('Wpisz liczbe wierszy: '))
n = int(input('Wpisz liczbe kolumn: '))
w = []  # Deklaruje liste
tab = [] # Deklaruje liste
for i in range(0,m): # Petla po wszystkich kolumnach
    for j in range(0,n): # Petla po wszystkich wierszach
        w.append(i*j)
    tab.append(w) 
    w = []
for i in range(0,m): # Petla po wszystkich kolumnach
    for j in range(0,n): # Petla po wszystkich wierszach
        print(tab[i][j], end=', ') # Wypisuje elementy tablicy. Rozdzielam je przecinkami
    print('')