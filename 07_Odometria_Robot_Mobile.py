from matplotlib import pyplot as plt
import pylab
import math
from Utils.Odometry import Odometry
from Utils.controllers import ControlloreProporzionaleIntegraleSat,ControlloreProporzionaleSat
from Utils.Robot import Robot
delta_t = 1e-3
t = 0
MassaRuotaDestra = Robot(3, 25.0)
MassaRuotaSinistra = Robot(3, 25.0)
B = 0.3 #cm distanza tra le due ruote
odometria = Odometry(B,MassaRuotaDestra,MassaRuotaSinistra)

#Definizione dei controller
cntrlRuotaDestra = ControlloreProporzionaleIntegraleSat(150, 400, 200)
cntrlRuotaSinistra = ControlloreProporzionaleIntegraleSat(150, 400, 200)
cntrlPos = ControlloreProporzionaleSat(1,1.5)
cntrlPosAng = ControlloreProporzionaleSat(5,4)

target_posx = 10
target_posy = 10
target_teta = 0
vettore_pos_sx = [ ]
vettore_pos_dx = [ ]
vettore_X = []
vettore_Y = []
vettore_distanza = []
vettore_tempi = [ ]
vettore_f = [ ]
vettore_v = []

while t<50:
    #Rileviamo la velocita corrente
    speed_motore_dx = MassaRuotaDestra.get_velocity()
    speed_motore_sx = MassaRuotaSinistra.get_velocity()
    #Odometria
    odometria.evaluate()
    #fase di controllo in posizione
    v,err = cntrlPos.evaluateErrorPos(odometria.getX(), odometria.getY(), target_posx, target_posy)
    if (err < 0.1):
        target_posx = 20
        target_posy = 15
    target_teta = math.atan2(target_posy - odometria.getY(), target_posx - odometria.getX())
    w = cntrlPosAng.evaluate(target_teta, odometria.getTeta())
    target_speed_Sx = v - (B * w) / 2
    target_speed_Dx = v + (B * w) / 2
    # Punto 3 --> PI ruota Sx
    velSx = cntrlRuotaSinistra.evaluate(target_speed_Sx, speed_motore_sx, delta_t)
    # Punto 4 --> PI ruota Dx
    velDx = cntrlRuotaDestra.evaluate(target_speed_Dx, speed_motore_dx, delta_t)
    # Punto 5 e 6
    # Aggiorno la posizione
    MassaRuotaSinistra.evaluate(velSx, delta_t)
    MassaRuotaDestra.evaluate(velDx, delta_t)

    # Aggiornamento vettore x e y
    vettore_X.append(odometria.getX())
    vettore_Y.append(odometria.getY())
    vettore_distanza.append(odometria.getDistanzaPercorsa())
    vettore_v.append(v)
    t = t + delta_t

    # Per il momento da non utilizzare, il target di posizione verrà implementato successivamente.
    # vettore_target.append(target_speed)
    vettore_tempi.append(t)

pylab.figure(1)
pylab.plot(vettore_X, vettore_Y, 'b-+', label='pos')
pylab.xlabel('X')
pylab.ylabel('Y')
pylab.legend()

pylab.figure(2)
pylab.plot(vettore_tempi, vettore_distanza, 'b-+', label='distanza')
pylab.xlabel('time')
pylab.legend()
pylab.show()

pylab.figure(3)
pylab.plot(vettore_tempi, vettore_v, 'b-+', label='vel')
pylab.xlabel('time')
pylab.legend()
pylab.show()