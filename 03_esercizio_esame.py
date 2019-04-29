from matplotlib import pyplot as plt

x1 = 0
x2 = 0
u = 3
K = 5
t = 0
delta_t = 1e-3
vettore_x1 = []
vettore_x2 = []
vettore_t = []

while t<20:
    x1_temp = x1
    x1 = x1 + delta_t*x2
    x2 = (1-3*delta_t)*x2 - K*delta_t*x1_temp +6*u
    t = t + delta_t
    vettore_x1.append(x1)
    vettore_x2.append(x2)
    vettore_t.append(t)

plt.subplot(1, 2, 1)
plt.title("x1")
plt.grid()
plt.plot(vettore_t, vettore_x1)
plt.subplot(1, 2, 2)
plt.title("x2")
plt.grid()
plt.plot(vettore_t, vettore_x2)

plt.show()