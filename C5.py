import numpy as np
import math
import matplotlib.pyplot as plt

V = np.eye(2)
u = np.array([-2,3])
F = -12

C1 = -u
r = np.sqrt(C1.T@C1-F)

len = 100
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + C1).T
plt.plot(x_circ[0,:],x_circ[1,:],label='$C$')

C2 = np.array([-3,2])

d = np.linalg.norm(C1-C2)

r2 = np.sqrt(d**2 + r**2)

print("Radius = ",end=" ")
print(r2)

len = 100
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r2*np.cos(theta)
x_circ[1,:] = r2*np.sin(theta)
x_circ = (x_circ.T + C2).T
plt.plot(x_circ[0,:],x_circ[1,:],label='$S$')

plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')


plt.show()
