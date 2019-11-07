
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

def y_icept(n,c):
	A = np.zeros(2)
	m_y = np.array([0,1])
	A[0] = 0
	A[1] = c/(n@m_y)
	return A
  
len = 50
omat = np.array([[0,1],[-1,0]]) 


P = np.array([-2,4]) 
Q = np.array([0,2]) 

mat = np.array([[0,1],[1,-1]])
c =  np.array([2,-4]) 

O = np.linalg.inv(mat)@c
r = np.linalg.norm(O-P)

print("Centre = ",end=" ")
print(O)
print("Radius = ",end=" ")
print(r)

#(i)
n_1 =  np.array([4,5]) 
c_1 =  6

#(ii)
n_2 =  np.array([2,-3]) 
c_2 =  -10

#(iii)
n_3 =  np.array([3,4]) 
c_3 =  3

#(iv)
n_4 =  np.array([5,2]) 
c_4 =  -4

if n_1@O == c_1:
	print('(i) is  a diameter')
else:
	print('(i) is not a diameter')

if n_2@O == c_2:
	print('(ii) is a diameter')
else:
	print('(ii) is not a diameter')

if n_3@O == c_3:
	print('(iii) is  a diameter')
else:
	print('(iii) is not a diameter')

if n_4@O == c_4:
	print('(iv) is  a diameter')
else:
	print('(iv) is not a diameter')


m_1 = omat@n_1
A_1 = y_icept(n_1,c_1)

m_2 = omat@n_2
A_2 =  y_icept(n_2,c_2)

m_3 = omat@n_3
A_3 =  y_icept(n_3,c_3)

m_4 = omat@n_4
A_4 =  y_icept(n_4,c_4)

k1=-0.7
k2=0.7

x_1= line_dir_pt(m_1,A_1,k1,k2)
x_2= line_dir_pt(m_2,A_2,k1,k2)
x_3= line_dir_pt(m_3,A_3,k1,k2)
x_4= line_dir_pt(m_4,A_4,k1,k2)


theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + O).T


plt.plot(x_1[0,:],x_1[1,:],label='$(i)$')
plt.plot(x_2[0,:],x_2[1,:],label='$(ii)$')
plt.plot(x_3[0,:],x_3[1,:],label='$(iii)$')
plt.plot(x_4[0,:],x_4[1,:],label='$(iv)$')
plt.plot(x_circ[0,:],x_circ[1,:],label='$C$')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')

plt.show()



