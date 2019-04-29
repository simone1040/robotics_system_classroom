#Il controllore proporzionale viene utilizzato per permettere al robot di arrivare ad una certa posizione
from Utils.controllers import ControlloreProporzionaleIntegrale
from Utils.Robot import Robot
from matplotlib import pyplot as plt
vel_target = 5
t = 0
delta_t = 1e-3

vett_vel = []
vettore_pos = []
vettore_temp = []

robot = Robot(6.0,25.0)
controllore_pi = ControlloreProporzionaleIntegrale(20, 30)

while t < 20:
    current_vel = robot.get_velocity()
    f = controllore_pi.evaluate(vel_target, current_vel, delta_t)
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