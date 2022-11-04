import math
#
# Zadanie 10
#

print('Zadanie 10')
elem = [] # Deklaruje liste
for i in range(100,401): # Tworze petle po wszystkich liczbach z przedzialu od 100 do 400
    j = str(i) # Tworze zmienna typu string z kazdej liczby
    flaga = 0 # Deklaruje flage, ktora pozwoli przerwac petle
    for k in range(len(j)): # Petla po wszystkich elementach w danej liczbie
        if int(j[k])%2 == 0: # Warunek sprawdzajacy czy cyfra jest podzielna na 2
            flaga = 1
        else:
            flaga = 0
            break
    if flaga == 1: # Warunek sprawdzajacy czy wszystkie cyfry sa podzielne przez 2
        elem.append(i)
print("Liczby o samych cyfrach parzystych to:")
print(elem, end=', ')
