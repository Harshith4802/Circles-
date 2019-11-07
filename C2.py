import numpy as np
import math
import matplotlib.pyplot as plt

P = np.array([2,2])

V = np.eye(2)
u = np.array([1,-2])
F = -4
  
c2=-u
r2=np.sqrt(c2.T@c2-F)

len = 100
theta = np.linspace(0,2*np.pi,len)
x_circ2 = np.zeros((2,len))
x_circ2[0,:] = r2*np.cos(theta)
x_circ2[1,:] = r2*np.sin(theta)
x_circ2 = (x_circ2.T + c2).T

plt.plot(x_circ2[0,:],x_circ2[1,:],label='$C_2$')

c1 = 2*P - c2
print(c1)
r1 = 3 
len = 100
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r1*np.cos(theta)
x_circ[1,:] = r1*np.sin(theta)
x_circ = (x_circ.T + c1).T
plt.plot(x_circ[0,:],x_circ[1,:],label='$C_1$')

m = np.array([1,0])
a=np.linalg.norm(m)**2
b=-2*(m.T@c1)
c=np.linalg.norm(c1)**2-r1**2
i1 = (-b+np.sqrt(b**2 - 4*a*c))/2*a  
i2 = (-b-np.sqrt(b**2 - 4*a*c))/2*a  
print("i1 = ",end=" ")
print(i1)
print("i2 = ",end=" ")
print(i2)
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')


plt.show()




