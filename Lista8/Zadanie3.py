import random
import sys

def pesel():

    year = random.randint(1800,2299) # Generuje losowo rok urodzin z przedzialu 1800,2299
    
    # Uwzgledniam rozne wartosci miesiaca w zaleznosci od wylosowanego roku
    if year <= 1999 and year > 1899:
        month = random.randint(1,12)
    elif year <= 1899:
        month = random.randint(1,12) + 80
    elif year >= 2000 and year < 2100:
        month = random.randint(1,12) + 20 
    elif year >= 2100 and year < 2200:
        month = random.randint(1,12) + 40
    elif year >= 2200:
        month = random.randint(1,12) + 60


	# Przypisuje mozliwe wartosci miesiecy do zmiennych
    odd_months = (1, 3, 5, 7, 8, 10, 12, 21, 23, 25, 27, 28, 30, 32, 41, 43, 45, 47, 48, 50, 52, 61, 63, 65, 67, 68, 70, 72, 81, 83, 85, 87, 88, 90, 92)
    even_months = (4, 6, 9, 11, 24, 26, 29, 31, 44, 46, 49, 51, 64, 66, 69, 71, 84, 86, 89, 91)
    
    # Przypisuje odpowiednim miesiaca 31 dni
    if month in odd_months:
        day = random.randint(1,31)
    
    # Przypisuje odpowiednim miesiaca 30 dni
    elif month in even_months:
        day = random.randint(1,30)		
	# Uwzgledniam miesiac luty
    else:
        if year % 4 == 0 and year != 1900 and year != 1800 and year != 2100 and year != 2200:
            day = random.randint(1,29) # rok przestepny

        else:
            day = random.randint(1,28) # rok zwyczajny

    # Losowanie 4 kolejnych cyfr
    four_random = random.randint(1000,9999)
    four_random = str(four_random)
    
    # Pobranie odpowiednich liczb z daty
    y = '%02d' % (year % 100)
    m = '%02d' % month
    dd = '%02d' % day

    a = y[0]
    a = int(a)

    b = y[1]
    b = int(b)

    c = m[0]
    c = int(c)

    d = m[1]
    d = int(d)

    e = dd[0]
    e = int(e)

    f = dd[1]
    f = int(f)

    g = four_random[0]
    g = int(g)

    h = four_random[1]
    h = int(h)

    i = four_random[2]
    i = int(i)

    j = four_random[3]
    j = int(j)
    
    # uwzglednienie wag poszczegolnych cyfr w peselu
    check = a + 3 * b + 7 * c + 9 * d + e + 3 * f + 7 * g + 9 * h + i + 3 * j
    if check % 10 == 0:
        last_digit = 0
    else:
        last_digit = 10 - (check % 10)

	# Wypisanie peselu
    return '%02d' % (year % 100)+'%02d' % month+'%02d' % day+four_random+str(last_digit)


# Tworzenie pliku i zapisanie peselow do pliku
with open('PESEL.txt', 'w') as f:
    sys.stdout = f
    for i in range(10):
        p = pesel()
        print(p)
    sys.stdout
