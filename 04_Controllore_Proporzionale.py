#Il controllore proporzionale viene utilizzato per permettere al robot di arrivare ad una certa posizione
from Utils.controllers import Controllore_Proporzionale
from Utils.Robot import Robot
from matplotlib import pyplot as plt
pos_target = 20
t = 0
delta_t = 1e-3

vett_vel = []
vettore_pos = []
vettore_temp = []

robot = Robot(6.0,25.0)
controllore_p = Controllore_Proporzionale(10)

while t < 20:
    current_pos = robot.get_position()
    f = controllore_p.evaluate(pos_target, current_pos)
    robot.evaluate(f, delta_t)
    t = t + delta_t
    vett_vel.append(robot.get_velocity())
    vettore_pos.append(robot.get_position())
    vettore_temp.append(t)

plt.subplot(1, 2, 1)
plt.title("Posizione")
plt.grid()
plt.plot(vettore_temp, vettore_pos)
plt.subplot(1, 2, 2)
plt.title("Velocita")
plt.grid()
plt.plot(vettore_temp,vett_vel)

plt.show()