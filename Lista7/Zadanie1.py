import math
import time

#
# Zadanie 1
#

print('Zadanie 1')

N = int(input("Podaj wartosc N: "))

def fib_iter(n):
    a = 0
    b = 1
    print(a, end=" ")
    while n+1 > 1:
        print(b, end=" ")
        a, b = b, a + b  # przypisanie wielokrotne
        n -= 1


def fib_rek(n):
    # Funkcja zwraca n-ty wyraz ciągu Fibonacciego
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib_rek(n - 1) + fib_rek(n - 2)

a = time.time()
fib_iter(N)
b = time.time()
print(" ")
print('Czas iteracji: ',b-a)
print(" ")
c = time.time()
for i in range(N+1):
    print(fib_rek(i), end=" ")
d = time.time()
print(" ")
print('Czas rekurencji: ',d-c)

# Dla malych N rekurencja może być szybsza ale wraz ze wzrostem N, znaczaco sie wydluza