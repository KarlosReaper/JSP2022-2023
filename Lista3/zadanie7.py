import math

#
# Zadanie 7
#
# Ciag Fibonaciego to suma dwoch poprzednich wyrazow, gdzie F0 = 0 i F1 = 1
print('Zadanie 7')
N = int(input('Wpisz numer wyrazu N: '))
a = 0 # Pierwszy wyraz ciagu
b = 1 # Drugi wyraz ciagu
print(a, end=" ") # Wypisuje pierwszy wyraz
while N > 0: # Powtarzam wszystki dopóki N > 0
    print(b, end=" ") # Wypisuje kolejne wyrazy
    a = b
    b = a + b 
    N -= 1
