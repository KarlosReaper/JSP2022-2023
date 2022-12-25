import datetime
import fileinput
import sys

def pesel_o():
    import datetime
    my_absolute_path2 = r'C:\Users\laptop\Desktop\Jezyki skryptowe - python\GitHub\Lista8\PESEL2.txt'
    ff = open(my_absolute_path2,'w')
    my_absolute_path = r'C:\Users\laptop\Desktop\Jezyki skryptowe - python\GitHub\Lista8\PESEL.txt'
    with open(my_absolute_path, 'r', encoding='utf-8') as plik: # otworzenie pliku do odczytu
        month1 = (81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92)
        month2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        month3 = (21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32)
        month4 = (41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52)
        month5 = (61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72)
        while 1: # nieskonczony while
            pobranie = plik.readline() # czytanie pliku po linii
            if not pobranie: # zakoncz petle jezeli nie ma juz lini w pliku
                break 
            else:
                # uwzglednienie wag poszczegolnych cyfr w peselu
                check = int(pobranie[0])+3*int(pobranie[1])+7*int(pobranie[2])+9*int(pobranie[3])+int(pobranie[4])+3*int(pobranie[5])+7*int(pobranie[6])+9*int(pobranie[7])+int(pobranie[8])+3*int(pobranie[9])
                if check % 10 == 0:
                    last_digit = 0
                else:
                    last_digit = 10 - (check % 10)

                if last_digit == int(pobranie[10]):
                    pobranie = pobranie[0:10]
                    p = int(pobranie[9]) %2 # pobranie 10 elementu z peselu okreslajacego plec wlasciciela
                    r = int(pobranie[0:2]) # pobranie koncowki roku z poczatku peselu
                    m = int(pobranie[2:4]) # miesiac
                    d = int(pobranie[4:6]) # dzien
                    if p == 1: #parzyste mezczyzni
                        plec = "M"
                    else:
                        plec = "K"
                    if m in month1:
                        rok = r+1800
                        miesiac = m-80
                    elif m in month2:
                        rok = r+1900
                        miesiac = m
                    elif m in month3:
                        rok = r+2000
                        miesiac = m-20
                    elif m in month4:
                        rok = r+2100
                        miesiac = m-40
                    elif m in month5:
                        rok = r+2200
                        miesiac = m-60
                    dzien = d
                    x = datetime.date(rok, miesiac, dzien)
                    ff.write(pobranie+' '+x.strftime("%d-%m-%Y")+' plec '+plec+'\n') 
                else:
                    ff.write('Bledny pesel\n')
    ff.close()





pesel_o()
