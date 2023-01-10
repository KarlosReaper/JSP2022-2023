import xml.etree.ElementTree as ET

class Kursy:
	def __init__(self,sciezka):
		self.sciezka = sciezka
		
	def czytaj(self,sciezka):
		root = ET.parse(self.sciezka).getroot()
		return root
		
	# Wczytanie nazw walut
	def nam(self):
		root = self.czytaj(self.sciezka)
		nazwa = [n.text for n in root.findall('.//nazwa_waluty')]
		return nazwa
	
	# Wczytanie kodow walut
	def cod(self):
		root = self.czytaj(self.sciezka)
		kod = [k.text for k in root.findall('.//kod_waluty')]
		return kod
	
	# Wczytanie kursu walut
	def curse(self):
		root = self.czytaj(self.sciezka)
		kurs = [float(kk.text.replace(',','.')) for kk in root.findall('.//kurs_sredni')]
		return kurs 
	
	# Wczytanie wartosci kursow
	def dict(self):
		dic1 = {}
		dic2 = {}
		keys1 = self.nam()
		keys2 = self.cod()
		values = self.curse()
		k = 0
		for i in keys1:
			dic1[i] = values[k]
			k += 1
		k = 0
		for i in keys2:
			dic2[i] = values[k]
			k += 1
		return dic1,dic2

	# Przeliczanie walut z i na PLN	
	def pln(self,v1,wal1,wal2):
		dic1,dic2 = self.dict()
		if wal1 == 'PLN':
			v2 = v1/dic2[wal2]
		else:
			v2 = v1*dic2[wal1]
		return v2
	
	# Przeliczanie walut innych jak PLN
	def change(self,v1,wal1,wal2):
		dic1,dic2 = self.dict()
		wal1_pln = v1*dic2[wal1]
		pln_wal2 = wal1_pln/dic2[wal2]
		return pln_wal2

path = r'C:\Users\laptop\Desktop\Jezyki skryptowe - python\GitHub\Lista10/waluty.xml'
waluta = Kursy(path)
lista1 = waluta.nam()
lista2 = waluta.cod()
a = input('Czy wyswietlic liste dostepnych walut? Jesli tak to wpisz "waluty", jesli nie to wpisz kwote do zamienienia: ')
if a == 'waluty':
    print('Lista dostępnych walut:\n')
    for n,c in zip(lista1,lista2):
        print('{} ({})'.format(n,c))
else:
    kwota = int(a)
    aa = input('Podaj kody walut do przeliczenia (Jesli jedna z walut to PLN wtedy pomin ja i wpisz tylko druga): ')
    if len(aa) < 6:
        waluta0 = aa[0:3]
        wartosc1 = waluta.pln(kwota,'PLN',waluta0)
        print('\nKonwersja {} PLN na {}: {} {}'.format(kwota,waluta0,wartosc1,waluta0))

        wartosc2 = waluta.pln(kwota,waluta0,'PLN')
        print('Konwersja {} {} na PLN: {} PLN'.format(kwota,waluta0,wartosc2,waluta0))
    else:
        waluta1 = aa[0:3]
        waluta2 = aa[-3:]
        wartosc = waluta.change(kwota,waluta1,waluta2)
        wartosc3 = waluta.change(kwota,waluta2,waluta1)
        print('Konwersja {} {} na {}: {} {}'.format(kwota,waluta1,waluta2,wartosc,waluta2))
        print('Konwersja {} {} na {}: {} {}'.format(kwota,waluta2,waluta1,wartosc3,waluta1))



