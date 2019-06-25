from System import System
from PID import PID,reference
import pylab
t = 0
delta_t = 1e-3
tempi = []
output = []
ref_array = [ ]
y = 0
sistema = System()
controller = PID(4,10,50)
ref = reference()

while t < 20:
    ref_sig = ref.evaluate(t)
    error = ref_sig - y
    controller_output = controller.evaluate(error,delta_t)
    y = sistema.evaluate(controller_output, delta_t)
    ref_array.append(ref_sig)
    output.append(y)
    tempi.append(t)
    t = t + delta_t

pylab.figure(1)
pylab.plot(tempi, output, 'r-+', label='output')
pylab.plot(tempi, ref_array, 'b-+', label='input')
pylab.xlabel('time')
pylab.legend()

pylab.show()