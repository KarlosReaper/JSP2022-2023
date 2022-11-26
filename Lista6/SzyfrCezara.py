# ord() zwraca wartosc liczbowa danego symbolu
# chr() zwraca symbol dla danej wartosci liczbowej

def szyfruj(txt,KLUCZ):
    zaszyfrowny = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 96 and ord(txt[i]) < 123-KLUCZ:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ)
        elif ord(txt[i]) >= 123-KLUCZ and ord(txt[i]) < 123:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ -26)
        else:
            zaszyfrowny += txt[i]
    return zaszyfrowny

def deszyfruj(txt,KLUCZ):
    zaszyfrowny = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 96+KLUCZ and ord(txt[i]) < 123:
            zaszyfrowny += chr(ord(txt[i]) - KLUCZ)
        elif ord(txt[i]) > 96 and ord(txt[i]) < 97+KLUCZ:
            zaszyfrowny += chr(ord(txt[i]) - KLUCZ +26)
        else:
            zaszyfrowny += txt[i]
    return zaszyfrowny
