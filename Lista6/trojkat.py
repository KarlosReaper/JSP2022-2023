def spr(a,b,c):
    if a+b > c and a+c > b and b+c > a:
        print('Trojkat istnieje')
        return 1
    else:
        print('Trojkat nie istnieje')
        return 0

def obwod(a,b,c):
    obw = a+b+c
    return obw

def pole(a,b,c):
    import math
    p = (a+b+c)/2
    pole = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return pole

def rodzaj(a,b,c):
    if a == b and a == c:
        return "Trojkat jest rownoboczny"
    elif a == b and a != c:
        return "Trojkat jest rownoramienny"
    elif b == c and a != c:
        return "Trojkat jest rownoramienny"
    else:
        return "Trojkat jest roznoboczny"

def kat(a,b,c):
    dmax = max([a,b,c])
    if a == dmax:
        if b**2+c**2 == a**2:
            return "Trojkat jest prostokatny"
        if b**2+c**2 > a**2:
            return "Trojkat jest ostrokatny"
        if b**2+c**2 < a**2:
            return "Trojkat jest rozwartokatny"
    elif b == dmax:
        if a**2+c**2 == b**2:
            return "Trojkat jest prostokatny"
        if a**2+c**2 > b**2:
            return "Trojkat jest ostrokatny"
        if a**2+c**2 < b**2:
            return "Trojkat jest rozwartokatny"
    elif c == dmax:
        if a**2+b**2 == c**2:
            return "Trojkat jest prostokatny"
        if a**2+b**2 > c**2:
            return "Trojkat jest ostrokatny"
        if a**2+b**2 < c**2:
            return "Trojkat jest rozwartokatny"