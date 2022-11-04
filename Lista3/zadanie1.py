from ast import arg
import math

#
# Zadanie 1
#
print('Zadanie 1')
litera    = input('Podaj litere ')
samogloski = 'AEIOUÓYĄĘaeiouóyąę'
spolgloski = 'bcćdfghjklmnprstwyzżź'
if litera in samogloski:  # sprawdzam czy podana litera jest samogloska
    print("Podana litera jest samogloska")
elif litera in spolgloski:   # sprawdzam czy podana litera jest spolgloska
    print("Podana litera jest spolgloska")
elif litera not in spolgloski and litera not in samogloski: # jesli wprowadzony znak nie jest litera to wypisuje informacje o blednym znaku
    print("Podano bledny znak")
