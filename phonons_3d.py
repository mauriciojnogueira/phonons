import matplotlib.pyplot as plt
from cycler import cycler
import numpy as np
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import axes3d

import scipy as sp

''' Polarization '''
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x, y, z = np.meshgrid(np.arange(-1, 1, 0.1), np.arange(-1, 1, 0.1), np.arange(-1, 1, 0.1))

r = np.zeros((len(x), len(y), len(z)))
s = np.zeros((len(x), len(y), len(z)))
t = np.zeros((len(x), len(y), len(z)))

u = np.zeros((len(x), len(y), len(z)))
v = np.zeros((len(x), len(y), len(z)))
w = np.zeros((len(x), len(y), len(z)))

for i in range(len(x)):
    if i%4 == 0:
        r[10, 10, 10] = 0
        s[10, 10, 10] = i/10
        t[10, 10, 10] = np.sqrt(1 - (i/10)**2)

        ax.quiver(x, y, z, r, s, t, color='r')
        ax.quiver(x, y, z, r, -s, -t, color='r')
        ax.quiver(x, y, z, r, -s, t, color='r')
        ax.quiver(x, y, z, r, s, -t, color='r')

u[10, 0, 10] = 2

ax.quiver(x, y, z, u, v, w)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

''' Density of States (gold) '''

a_Au = 4.065e-10 # lattice parameter Au (m)
v_Au = 3240 # speed of sound Au (m/s)
w_D_Au = 3.9 * v_Au / a_Au

a_Al = 4.046e-10
v_Al = 6420
w_D_Al = 3.9 * v_Al / a_Al

def z(w, a, v):
    w_D = 3.9 * v / a
    w = [omega for omega in w if omega <= w_D]
    w = np.array(w)
    print(w_D)
    
    return w, (3 * w**2 / w_D**3)

w = np.linspace(1e13, 7e13, num=500)

w_Au, dist_Au = z(w, a_Au, v_Au)
w_Al, dist_Al = z(w, a_Al, v_Al)

fig2, ax2 = plt.subplots()

ax2.plot(w_Au, dist_Au, label='Au DOS')
ax2.plot(w_Al, dist_Al, label='Al DOS')
ax2.axvline(x=w_D_Au, linestyle='--', color='k')
ax2.axvline(x=w_D_Al, linestyle='--', color='k')
ax2.set_title(r'Density of States $z(\omega)$')
ax2.set_xlabel(r'$\omega$')
ax2.set_ylabel(r'$z$')
ax2.legend()

plt.show()