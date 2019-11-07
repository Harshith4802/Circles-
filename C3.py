import numpy as np
import math
import matplotlib.pyplot as plt

def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,3,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB



#Circle parameters
V = np.eye(2)
u = np.array([0,0])
F = -9

#defining centre and radius of Circle C1
c=-u
r=np.sqrt(c.T@c-F)

#Generating points on the circle C1
len = 100
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + c).T
plt.plot(x_circ[0,:],x_circ[1,:],label='$C$')

A1 = np.array([r*np.cos(4),r*np.sin(4)])
A2 = np.array([r*np.cos(3.5),r*np.sin(3.5)])
A3 = np.array([r*np.cos(5),r*np.sin(5)])
P = np.array([4,7])
plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1 + 0.1),P[1]*(1 - 0.1),'P')
plt.plot(A1[0],A1[1],'o')
plt.text(A1[0]*(1 + 0.1),A1[1]*(1 - 0.1),'A1')
plt.plot(A2[0],A2[1],'o')
plt.text(A2[0]*(1 + 0.1),A2[1]*(1 - 0.1),'A2')
plt.plot(A3[0],A3[1],'o')
plt.text(A3[0]*(1 + 0.1),A3[1]*(1 - 0.1),'A3')

#Generating all lines
x_1 = line_gen(A1,P)
x_2 = line_gen(A2,P)
x_3 = line_gen(A3,P)

#Plotting all lines
plt.plot(x_1[0,:],x_1[1,:],label='$L1$')
plt.plot(x_2[0,:],x_2[1,:],label='$L2$')
plt.plot(x_3[0,:],x_3[1,:],label='$L3$')

plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()
