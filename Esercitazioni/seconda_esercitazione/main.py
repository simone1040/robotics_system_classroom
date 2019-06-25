from System import System
import pylab
t = 0
delta_t = 1e-3
tempi = []
output = []
u = 1
sistema = System()

while t < 20:
    output.append(sistema.evaluate(u, delta_t))
    tempi.append(t)
    t = t + delta_t

pylab.figure(1)
pylab.plot(tempi, output, 'r-+', label='output')
pylab.xlabel('time')
pylab.legend()

pylab.show()

#DAl grafico notiamo che Il sistema si presenta Asintoticamente stabile ed in particolare il valore a regime è pari a 4