#
# Zadanie 3
#

print('Zadanie 3')

cyfry = ['0','1','2','3','4','5','6','7','8','9']

a = int(input('Podaj liczbe do utworzenia ciagu: '))

def look(a):
    a = str(a)
    dlugosc = len(a)
    j = 0
    li = []
    ni = []
    f = ''
    if dlugosc == 1:
        i = 0
        b = a[i]
        j = j+1
        li = li+[b]
        ni = ni+[j]
        f=f+str(ni[i])+str(cyfry[int(li[i])])
    else:
        for i in range(dlugosc):
            if a[i] in cyfry and i == 0:
                b = a[i]
                j = j+1
            elif a[i] in cyfry and i > 0:
                if b == a[i]:
                    j = j+1
                    if i == dlugosc-1:
                        li = li+[b]
                        ni = ni+[j]
                else:
                    li = li+[b]
                    ni = ni+[j]
                    b = a[i]
                    j = 1
                    if i == dlugosc-1:
                        li = li+[b]
                        ni = ni+[j]
        for i in range(len(li)):
            f=f+str(ni[i])+str(cyfry[int(li[i])])
    return f

c = a
a = 1
print(a)
for i in range(c):
    g = look(a)
    print(g)
    a = g
