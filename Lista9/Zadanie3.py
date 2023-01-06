import math
import numpy
import matplotlib.pyplot as plt

#
# Zadanie 3
#
print('Zadanie 3')

predkosc0 = int(input('Podaj wartosc poczatkowa predkosci [m/s]: '))
kat = int(input('Podaj kat nachylenia w stopniach: '))*math.pi/180.0

g = 9.81

hmax = predkosc0**2*math.sin(kat)**2/(2*g)
czas = 2*predkosc0*math.sin(kat)/g
zasieg = predkosc0**2*math.sin(2*kat)/g

print('Wysokosc maksymalna [m] = ',hmax,'\n','Czas lotu [s] = ',czas,'\n','Zasieg rzutu [m] = ',zasieg,'\n')

for i in range(101):
    if i == 0:
        tt = czas/100.0*i
        t = [tt]
        vx = [predkosc0*math.cos(kat)]
        vy = [predkosc0*math.sin(kat)-g*tt]
        xt = [predkosc0*math.cos(kat)*tt]
        yt = [predkosc0*math.sin(kat)*tt-g*tt**2/2]
        yx = [xt[i]*math.tan(kat)*xt[i]**2*g/(2*predkosc0**2*math.cos(kat)**2)]
        p  = [math.sqrt(xt[i]**2+yt[i]**2)]
    else:
        tt = czas/100.0*i
        t.append(tt)
        vx.append(predkosc0*math.cos(kat))
        vy.append(predkosc0*math.sin(kat)-g*tt)
        xt.append(predkosc0*math.cos(kat)*tt)
        yt.append(predkosc0*math.sin(kat)*tt-g*tt**2/2)
        yx.append(xt[i]*math.tan(kat)-xt[i]**2*g/(2*predkosc0**2*math.cos(kat)**2))
        p.append(math.sqrt(xt[i]**2+yt[i]**2))

tab_t  = numpy.array(t)
tab_vx = numpy.array(vx)
tab_vy = numpy.array(vy)
tab_xt = numpy.array(xt)
tab_yt = numpy.array(yt)
tab_yx = numpy.array(yx)
tab_p  = numpy.array(p)


plt.subplot(1, 3, 1)
plt.plot(tab_t,tab_vy,label='pionowa')
plt.plot(tab_t,tab_vx,label='pozioma')
plt.title("Predkosci chwilowe ")
plt.legend()
plt.xlabel('Czas [s]')
plt.ylabel('Predkosc [m/s]')

plt.subplot(1, 3, 2)
plt.plot(tab_t,tab_p)
plt.title("Polozenie")
plt.xlabel('Czas [s]')
plt.ylabel('Odleglosc [m]')

plt.subplot(1, 3, 3)
plt.plot(tab_xt,tab_yx)
plt.title("Tor ruchu")
plt.ylabel('Wysokosc [m]')
plt.xlabel('Odleglosc pozioma [m]')

plt.show()

# predkosci
#vx = predkosc0*math.cos(kat)
#vy = predkosc0*math.sin(kat)-g*t

# wspolrzedne polozenia
#xt = predkosc0*math.cos(kat)*t
#yt = y0+predkosc0*math.sin(kat)*t-g*t**2/2

# tor 
#xt = predkosc0*math.cos(kat)*t
#yx = y0+xt*math.tan(kat)*xt**2*g/(2*predkosc0**2*math.cos(kat)**2)