from math import factorial

#
# Zadanie 7
#
print('Zadanie 7')

# Definiuję funkcję do tworzenia trójkąta Pascala
def pascal(n):
  # Pętla po całym zakresie zadanego n
  for i in range(n):
    # Pętla do zapewnienia odpowiednich przerw
	  for j in range(n-i+1):
		  print(end=" ")
    
    # Pętla do obliczenia odpowiednich elementów i zapełnienia trójkąta, rodziela elementy tabulacją
	  for j in range(i+1):
		  print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
	  # Zapewnienie podziału na nowe linie 
	  print("")

# Wczytanie liczby wierszy
n = int(input("Podaj wiersz trojkata Pascala: "))

# Wypisanie trójkąta Pascala
pascal(n)
