import re

#
# Zadanie 5
#
print('Zadanie 5')
# pakiet re pozwala na sprawdzanie czy dany znak występuje w zmiennej
def password(haslo):
    liczba = re.compile(r'.{6,}')    #powyzej 6 znakow
    duze = re.compile(r'[A-Z]+')   # conajmniej 1 duza litera
    male = re.compile(r'[a-z]+')    # conajmniej 1 mala litera
    znaki = re.compile(r'[@$#]+')    # conajmniej 1 znak
    liczby = re.compile(r'[\d]+')     # conajmniej 1 cyfra
    if liczba.search(haslo):# and hasloRegex_duze.search(haslo) and hasloRegex_male.search(haslo) and hasloRegex_liczby.search(haslo):
        if duze.search(haslo):
            if male.search(haslo):
                if liczby.search(haslo):
                    if znaki.search(haslo): 
                        if len(haslo) <= 16:  # sprawdzam czy liczba znakow jest nie wieksza jak 16
                            print('Haslo jest poprawne')
                        else:
                            print('Za duza liczba znakow')
                    else:
                        print('Brak znakow specjalnych: #$@')
                else:
                    print("Brak liczb")
            else:
                print('Brak malych liter')
        else:
            print('Brak wielkich liter')
    else:
        print('Za malo znakow')	

haslo = input('Wpisz haslo: ')
password(haslo)