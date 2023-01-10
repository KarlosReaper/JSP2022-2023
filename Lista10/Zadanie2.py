from itertools import combinations

#
# Zadanie 2
#

print('Zadanie 2')

class podlisty:
    def __init__(self,lista):
        comb = []
        for i in range(len(lista)+1):
            comb += [list(j) for j in combinations([1, 2, 3], i)]
        self.listy = comb


lst = []
# Liczba elementow listy
n = int(input("Enter number of elements : "))

# Wczytanie elementow listy
for i in range(0, n):
	ele = int(input())
	lst.append(ele)	

lista = lst
k = podlisty(lista) # przypisuje do k klase z podstawiona lista
print('Podlisty to: ', k.listy)