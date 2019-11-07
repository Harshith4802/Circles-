import numpy as np
import math
import matplotlib.pyplot as plt

def reflection(m,n,A,c):
 n=n.reshape((2,1))
 m=m.reshape((2,1))
 B = (((m@m.T-n@n.T)/(m.T@m+n.T@n))@A) + ((c*n)/(np.linalg.norm(n))**2).reshape(1,2)
 return B
  
def line_dir_pt(m,A,k1,k2):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB
  
V = np.eye(2)
u = np.array([-2,0])
F = 0
  
C1=-u/2
r1=np.sqrt(C1.T@C1-F)
r2=np.sqrt(C1.T@C1-F)
n = np.array([1,1])
omat = np.array([[0,1],[-1,0]])  
m = omat@n
c=3


C2 = 2*reflection(m,n,C1,c)

print("Radius = ",end=" ")
print(r2)
print("Centre = ",end=" ")
print(C2)
len = 100
theta = np.linspace(0,2*np.pi,len)
x_circ2 = np.zeros((2,len))
x_circ2[0,:] = r2*np.cos(theta)
x_circ2[1,:] = r2*np.sin(theta)
x_circ2 = (x_circ2.T + C2).T

plt.plot(x_circ2[0,:],x_circ2[1,:],label='$C_2$')

len = 100
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r1*np.cos(theta)
x_circ[1,:] = r1*np.sin(theta)
x_circ = (x_circ.T + C1).T
plt.plot(x_circ[0,:],x_circ[1,:],label='$C_1$')

p=np.array([3,0])
T = line_dir_pt(m,p,-3,2)
plt.plot(T[0,:],T[1,:],label='$Line$')

plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')


plt.show()
