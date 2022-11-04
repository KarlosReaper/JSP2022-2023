from ast import arg
import math

#l=['*',' ','*',' ','*',' ','*',' ','*',' ','*',' ','*****', sep='\n']
#print(l, sep='\n')
L = [
  ['*', '', '*', '', '*', '', '*', '', '*', '', '*', '', '*'],
  ['', '', '', '', '', '', '', '', '', '', '', '', '*'],
  ['', '', '', '', '', '', '', '', '', '', '', '', '*'],
  ['', '', '', '', '', '', '', '', '', '', '', '', '*'],
  ['', '', '', '', '', '', '', '', '', '', '', '', '*']]
#for j in range(5): # Petla po wszystkich kolumnach
#    for i in range(13): # Petla po wszystkich wierszach
#        print(L[j][i]) # Wypisuje elementy tablicy. Rozdzielam je przecinkami
#    print('')
L = [ # Tworze litere L z gwiazdek na wysokosc 7
  ['*', ' ', ' ', ' ', ' '],
  ['*', ' ', ' ', ' ', ' '],
  ['*', ' ', ' ', ' ', ' '],
  ['*', ' ', ' ', ' ', ' '],
  ['*', ' ', ' ', ' ', ' '],
  ['*', ' ', ' ', ' ', ' '],
  ['*', '*', '*', '*', '*']
  ];
A = [ # Tworze litere A z gwiazdek na wysokosc 7
  [' ', ' ', ' ', ' ', ' ', ' ', '*',' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', '*', ' ','*', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', '*', ' ', ' ',' ', '*', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', '*', '*', '*', '*','*', '*', '*', ' ', ' ', ' '],
  [' ', ' ', '*', ' ', ' ', ' ', ' ',' ', ' ', ' ', '*', ' ', ' '],
  [' ', '*', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', '*', ' '],
  ['*', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', '*']
  ];
R = [ # Tworze litere R z gwiazdek na wysokosc 7
  ['*', '*', '*', '*', ' '],
  ['*', ' ', ' ', ' ', '*'],
  ['*', ' ', ' ', ' ', '*'],
  ['*', '*', '*', '*', ' '],
  ['*', ' ', '*', ' ', ' '],
  ['*', ' ', ' ', '*', ' '],
  ['*', ' ', ' ', ' ', '*']
  ];
a=[]
b=[]
c=[]
#print(letter_F)
for i in range(7):
  for j in range(5):
   # print(letter_F[i][j], sep='\t')
    a.extend(L[i][j]) # tworze liste z pojedynczym wierszem litery L
    c.extend(R[i][j]) # tworze liste z pojedynczym wierszem litery R
  for j in range(13):
    b.extend(A[i][j]) # tworze liste z pojedynczym wierszem litery A
  print(a[0],a[1],a[2],a[3],a[4],' ',b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8],b[9],b[10],b[11],b[12],' ',c[0],c[1],c[2],c[3],c[4], sep='')
  a=[]
  b=[]
  c=[]