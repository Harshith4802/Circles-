import numpy as np
import math
import matplotlib.pyplot as plt
def line_dir_pt(m,A,k1,k2):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

A = np.array([2,3]) 
B = np.array([4,5])
n1 = np.array([-1,4])

m=A-B
C =(A+B)/2

n2 = np.array([1,1])
c =np.array([7,3])

R = np.vstack((n2,n1))

O = np.linalg.inv(R)@c.T


print(O)

r = np.linalg.norm(O-A)

print(r)

plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1 + 0.1),A[1]*(1 - 0.1),'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*(1 - 0.2),B[1]*(1),'B')
plt.plot(O[0],O[1],'o')
plt.text(O[0]*(1 + 0.1),O[1]*(1 - 0.1),'O')
T = line_dir_pt(m,O,-2,3)
plt.plot(T[0,:],T[1,:],label='$Line through centre$')
len = 100
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + O).T
plt.plot(x_circ[0,:],x_circ[1,:],label='$C_1$')
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()
