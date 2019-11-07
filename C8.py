import numpy as np
import matplotlib.pyplot as plt

def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return omat@dir_vec(A,B)

#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

dvec = np.array([-1,1]) 
omat = np.array([[0,1],[-1,0]]) 

def point(A, label=''):
	plt.plot(A[0], A[1], 'o')
	if label != '':
		plt.text(A[0], A[1], label)
		
def line_pts(A, B, labelA='', labelB=''):
	x_AB = line_gen(A,B)
	plt.plot(x_AB[0,:], x_AB[1,:],label='$'+labelA+labelB+'$');
	point(A, labelA)
	point(B, labelB)


def draw_circle(O, r, label="", len=100):
	x = np.zeros((2,len))
	theta = np.linspace(0, 2*np.pi, len)
	x[0,:] = O[0] + (r*np.cos(theta))
	x[1,:] = O[1] + (r*np.sin(theta))
	plt.plot(x[0,:], x[1,:], label=label)
	
def line_circ_int(O,r,P,m):
 a = m@m
 b = 2 * m@(P - O)
 c = P@P + O@O - 2 * P@O - r**2
 disc = b**2 - 4 * a * c
 lam1 = (-b + np.sqrt(disc)) / (2 * a)
 lam2 = (-b - np.sqrt(disc)) / (2 * a)
 return np.array([P+ lam1*m, P + lam2*m])

O =np.array([3, -2])
r = 5
draw_circle(O,r)

c = np.array([0,1])

# for m=2
m = np.array([1,2])
P,Q = line_circ_int(O,r,c,m)
line_pts(P,Q,'P','Q')
point(c, 'C')
plt.axis('equal')
plt.grid()
plt.show()
