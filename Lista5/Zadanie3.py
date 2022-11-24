from ast import arg
import math

#
# Zadanie 3
#
print('Zadanie 3')


def dziesietne(rzym):
    symbole = ["I","V","X","L","C","D","M"]
    jednosci = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    dziesiatki = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    setki = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM", "M", "MM", "MMM"]
    wj = ["1","2","3","4","5","6","7","8","9"]
    wd = ["10","20","30","40","50","60","70","80","90"]
    ws = ["100","200","300","400","500","600","700","800","900","1000","2000","3000"]

    dlugosc = len(rzym)

    for i in range(dlugosc):
        if rzym[i] not in symbole:
            return 0

    j = 0
    b = []
    for i in range(dlugosc):
        if j > 0:
            j = j-1
        else:
            if i+3 in range(dlugosc):
                a = rzym[i]+rzym[i+1]+rzym[i+2]+rzym[i+3]
                if a in jednosci:
                    j=3
                    b = b+[a]
                elif a in dziesiatki:
                    j=3
                    b = b+[a]
                elif a in setki:
                    j=3
                    b = b+[a]
                else:
                    a = rzym[i]+rzym[i+1]+rzym[i+2]
                    if a in jednosci:
                        j=2
                        b = b+[a]
                    elif a in dziesiatki:
                        j=2
                        b = b+[a]
                    elif a in setki:
                        j=2
                        b = b+[a]
                    else:
                        a = rzym[i]+rzym[i+1]
                    if a in jednosci:
                        j=1
                        b = b+[a]
                    elif a in dziesiatki:
                        j=1
                        b = b+[a]
                    elif a in setki:
                        j=1
                        b = b+[a]
                    else:
                        a = rzym[i]
                        if a in jednosci:
                            j=0
                            b = b+[a]
                        elif a in dziesiatki:
                            j=0
                            b = b+[a]
                        elif a in setki:
                            j=0
                            b = b+[a]
            elif i+2 in range(dlugosc):
                a = rzym[i]+rzym[i+1]+rzym[i+2]
                if a in jednosci:
                    j=2
                    b = b+[a]
                elif a in dziesiatki:
                    j=2
                    b = b+[a]
                elif a in setki:
                    j=2
                    b = b+[a]
                else:
                    a = rzym[i]+rzym[i+1]
                    if a in jednosci:
                        j=1
                        b = b+[a]
                    elif a in dziesiatki:
                        j=1
                        b = b+[a]
                    elif a in setki:
                        j=1
                        b = b+[a]
                    else:
                        a = rzym[i]
                        if a in jednosci:
                            j=0
                            b = b+[a]
                        elif a in dziesiatki:
                            j=0
                            b = b+[a]
                        elif a in setki:
                            j=0
                            b = b+[a]
            elif i+1 in range(dlugosc):
                a = rzym[i]+rzym[i+1]
                if a in jednosci:
                    j=1
                    b = b+[a]
                elif a in dziesiatki:
                    j=1
                    b = b+[a]
                elif a in setki:
                    j=1
                    b = b+[a]
                else:
                    a = rzym[i]
                    if a in jednosci:
                        j=0
                        b = b+[a]
                    elif a in dziesiatki:
                        j=0
                        b = b+[a]
                    elif a in setki:
                        j=0
                        b = b+[a]
            else:
                a = rzym[i]
                if a in jednosci:
                    j=0
                    b = b+[a]
                elif a in dziesiatki:
                    j=0
                    b = b+[a]
                elif a in setki:
                    j=0
                    b = b+[a]
        i=i+j
    wartosc=0
    dw=0
    ew=0
    df=0
    for i in range(len(b)):
        if b[i] in jednosci:
            d=jednosci.index(b[i])
            dw=int(wj[d])
        elif b[i] in dziesiatki:
            e=dziesiatki.index(b[i])
            ew=int(wd[e])
        elif b[i] in setki:
            f=setki.index(b[i])
            df=int(ws[f])
        wartosc = wartosc+dw+ew+df
        dw=0
        ew=0
        df=0
    return wartosc
    

rzym = input("Podaj liczbe rzymska (Koniecznie duze litery [w przypadku bledu zwraca 0]): ")
liczba = dziesietne(rzym)
print("Wartosc liczby to: ", liczba)