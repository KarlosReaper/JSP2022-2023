#
# Zadanie 3
#

print('Zadanie 3')

liczby = ['zera','jedynki','dwojki','trojki','czworki','piatki','szostki','siodemki','osemki','dziewiatki']
cyfry = ['0','1','2','3','4','5','6','7','8','9']

a = input('Podaj ciag liczb do przetworzenia: ')
dlugosc = len(a)

j = 0
li = []
ni = []
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
    

print(li)
print(ni)
for i in range(len(li)):
    print(ni[i], liczby[int(li[i])], end=" ")