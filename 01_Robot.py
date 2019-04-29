from matplotlib import pyplot as plt

F = 30
b = 6
v = 0
t = 0
M = 40
delta_t = 1e-3
p = 0
vett_vel = []
vett_tempi = []
vett_pos = []

while t < 20:
    t = t + delta_t
    temp_v = v
    v = v - (b/M)*v*delta_t + (1/M)*delta_t*F
    p = p+temp_v*delta_t
    vett_pos.append(p)
    vett_tempi.append(t)
    vett_vel.append(v)

plt.subplot(1,2,1)
plt.title("Posizione")
plt.grid()
plt.plot(vett_tempi,vett_pos)
plt.subplot(1,2,2)
plt.title("Velocita")
plt.grid()
plt.plot(vett_tempi,vett_vel)

plt.show()
