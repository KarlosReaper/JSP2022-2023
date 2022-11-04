from ast import arg
import math

#
# Zadanie 3
#
print('Zadanie 3')
a = int(input('współczynnik a ze wzoru ax^2+bx+c '))
if a == 0: # Sprawdzam czy rownanie jest kwadratowe (a nie moze byc rowne 0)
    print("To nie jest rownanie kwadratowe")
else:
    b = int(input('współczynnik b ze wzoru ax^2+bx+c '))
    c = int(input('współczynnik c ze wzoru ax^2+bx+c '))
    print("Wspolczynniki to: ", a, b, c)
    delta = b**2-4*a*c
    if delta < 0: # Sprawdzam czy delta jest ujemna (brak rozwiazan)
        print("Rownanie nie ma rozwiazan")
    elif delta == 0: # Sprawdzam czy delta jest rowna 0 (jedno rozwiazanie)
        print("Rozwiazanie rownania to x = ",-b/(2*a))
    elif delta > 0: # Sprawdzam czy delta jest wieksza od 0 (dwa rozwiazania)
        print("Rozwiazania rownania to x1 = ", (-b-math.sqrt(delta))/(2*a), " x2 = ", (-b+math.sqrt(delta))/(2*a))
