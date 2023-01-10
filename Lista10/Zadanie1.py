import math

class kolo:
    def __init__(self,r):
        self.pole, self.obwod = math.pi*r**2, 2*math.pi*r

r = int(input('Podaj promien kola: '))

k = kolo(r) # przypisuje do k klase z podstawionym promieniem r
print('Pole kola to: ', k.pole)
print('Obwod kola to: ', k.obwod)