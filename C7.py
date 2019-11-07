import numpy as np
import matplotlib.pyplot as plt

def line_dir_pt(m,A,k1,k2):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

P=np.array([1,-1])

n1=np.array([2,1])
omat = np.array([[0,1],[-1,0]])  
m1 = omat@n1
n2=np.array([1,-1])
m2 = omat@n2
X=np.zeros(2)
X[0]=3
X[1]=1

N=np.vstack((n1,n2))
O=np.linalg.inv(N)@X
print("Centre = ",end=" ")
print(O)
print("Radius = ",end=" ")
r = np.linalg.norm(O-P)
print(r) 
A = np.array([1.5,0]) 
B = np.array([1,0])
k1=1
k2=-1

x_1= line_dir_pt(m1,A,k1,k2)
x_2= line_dir_pt(m2,B,k1,k2)

plt.plot(x_1[0,:],x_1[1,:],label='$(i)$')
plt.plot(x_2[0,:],x_2[1,:],label='$(ii)$')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.1), P[1] * (1 - 0.1) , 'P')

len = 100
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + O).T
plt.plot(x_circ[0,:],x_circ[1,:],label='$C$')

n = O-P
m = omat@n
T = line_dir_pt(m,P,-3,4)
plt.plot(T[0,:],T[1,:],label='$T$')

plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()
