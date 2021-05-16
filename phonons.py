''' Phonons '''

import matplotlib.pyplot as plt
from cycler import cycler
import numpy as np
import matplotlib.animation as animation

''' Phonons in 1D '''

a = 4.065 # lattice parameter of Au
n = 7 # number of atoms
x = np.linspace(0, n*a, num=n+1) # position of each atom
t = np.linspace(0, 10, num=10000)

k = 6 * np.pi / (6*a) # wave number (pi/a is the biggest value for k)
lamb = 2 * np.pi / k
f = 10 # equivalent to elastic constant of a spring
m = 197 / 6.023e24 # mass of the atom

def omega_func(k, a, f, m):
    return np.sqrt(4*f/m) * np.sin(abs(k) * a / 2)

omega = omega_func(k, a, f, m)

def q(t, x, omega, a, phi=0):
    return a/2 * np.cos(omega*t + k*x + phi)

def vibration(t, x, omega, a):
    return x + q(t, x, omega, a)

print(lamb / a)
print(x)
print(t[50])
print(q(t[50], x, omega, a))
print(vibration(t[50], x, omega, a))

def animation2(i, t, x, omega, a):
    ax.clear()
    ax.set_xlim([-a, (n+1)*a])
    ax.plot(vibration(t[i], x, omega, a), np.zeros(len(x)), marker='o', linestyle='', color='k')
    #ax.plot(vibration(t[i], x[0], omega, a), 0, marker='o', linestyle='', color='k')
    ax.plot(x, np.zeros(len(x)), color='red', marker='o', mfc='None', linestyle='')
    ax.axhline(y=0, linestyle='--', color='b')
    ax.set_title('Phonons 1D')


fig, ax = plt.subplots()

animation_1d = animation.FuncAnimation(fig, animation2, frames=range(1, len(t)), fargs=(t, x, omega, a), interval=100)

fig2, ax2 = plt.subplots()

k1 = np.linspace(-np.pi / a, 0)
k2 = np.linspace(0, np.pi / a)

ax2.plot(k1, omega_func(k1, a, f, m), linestyle='--', color='r')
ax2.plot(k2, omega_func(k2, a, f, m), color='r')
ax2.set_title('Dispersion')
ax2.set_xlabel(r'$k$')
ax2.set_ylabel(r'$\omega$')
ax2.axhline(y=0, color='k')
ax2.axvline(x=np.pi/a, linestyle='--', color='k', label=r'$\pi/a$')
ax2.legend()

plt.show()