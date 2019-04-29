from matplotlib import pyplot as plt
t = 0
delta_t = 1e-3
w = 0.0
theta = 0.0
g = 9.8
F = 30
b = 100
M = 40

vettore_vel = []
vettore_temp = []
vettore_pos = []

while t<20:
    theta_temp = theta
    theta = theta + w*delta_t
    w = w - (b/M)*w*delta_t - g*theta_temp*delta_t + (delta_t/M)*F
    t = t + delta_t
    vettore_vel.append(w)
    vettore_pos.append(theta)
    vettore_temp.append(t)

plt.subplot(1,2,1)
plt.title("Posizione")
plt.grid()
plt.plot(vettore_temp,vettore_pos)
plt.subplot(1,2,2)
plt.title("Velocita")
plt.grid()
plt.plot(vettore_temp,vettore_vel)

plt.show()