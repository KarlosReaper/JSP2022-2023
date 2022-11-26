import SzyfrCezara

#
# Zadanie 2
#

print('Zadanie 2')

klucz = int(input("Podaj wartosc liczbowa do szyfrowania (1-26 [inaczej pojawia sie inne znaki ale tez zadziala]): "))
text = input("Podaj zdanie do zaszyfrowania [szyfrowaniu ulegaja tylko litery]: ")
a = SzyfrCezara.szyfruj(text, klucz)
print("Zaszyfrowane zdanie: ",a)
b = SzyfrCezara.deszyfruj(a,klucz)
print("Odszyfrowane zdanie: ", b)