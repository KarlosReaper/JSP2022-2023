from ast import arg
import math

#
# Zadanie 4
#
print('Zadanie 4')

tekst0 = "to jest moj tekst"
tekst = "a to jest moj tekst a nie twoj"
tekst2 = "Napisz funkcje do szyfrowania i deszyfrowania tekstu. Przetestuj szyfrowanie i deszyfrowanie na kilku przykladach."
tekst3 = "Dany jest szyfr, który zamienia samogloski wg klucza: klucz"


def szyfr(tekst2):
    tekst = list(tekst2)
    dlugosc = len(tekst)
    a = []
    e = []
    i = []
    o = []
    y = []
    for j in range(dlugosc):
        if tekst[j] == "a":
            a = a+[j]
        elif tekst[j] == "e":
            e = e+[j]
        elif tekst[j] == "i":
            i = i+[j]
        elif tekst[j] == "o":
            o = o+[j]
        elif tekst[j] == "y":
            y = y+[j]
    if len(a) > 0:
        for j in range(len(a)):
            tekst[a[j]] = 'y'
    if len(e) > 0:
        for j in range(len(e)):
            tekst[e[j]] = 'i'
    if len(i) > 0:
        for j in range(len(i)):
            tekst[i[j]] = 'o'
    if len(o) > 0:
        for j in range(len(o)):
            tekst[o[j]] = 'a'
    if len(y) > 0:
        for j in range(len(y)):
            tekst[y[j]] = 'e'
    tekst3 = "".join(tekst)
    print("Zdanie ("+tekst2+") po zaszyfrowaniu to: "+tekst3)

szyfr(tekst0)
szyfr(tekst)
szyfr(tekst2)
szyfr(tekst3)