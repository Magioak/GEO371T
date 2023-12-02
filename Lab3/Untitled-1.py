# %%
import numpy as np
from IPython.display import display, Math


B = np.array([[1,2,-3],[3,4,-1]])
A = np.array([[2,-5,1],[1,4,5],[2,-1,6]])
y = np.array([2,-4,1])
z = np.array([-15,-8,-22])
x = 'AB'
k = 'T'
print('(a)\n\n BA \n',B@A ,'\n\n')



# %%
print('(b)')
display(Math(x + '^{'+ k +'}'))
print(A@B.T,'\n\n')

# %%
print('(c)\n\n Ay\n', A@y)

# %%
print('(D)\n\n y^Tz \n',np.inner(y,z))


# %%
print('(e)\n\nyz^T\n', np.outer(y,z))



# %%
import scipy.linalg as la 
from scipy.linalg import solve

#Problem 2

A = np.array([[1,2],[3,0]])
b = np.array([4,6])

print('(a)\n\n A^-1\n', la.inv(A))
print('\nAA^-1\n',A@la.inv(A))

# %%
x = solve(A,b)
print ('x\n',x)
print('\n\nproving Ax = b by Ax -b = 0\n',np.dot(A,x)-b)

# %%
import matplotlib.pyplot as plt


#Problem 3
A = np.array([[2,0],[0,2]])
B = np.array([[-2,0],[0,2]])
C = np.array([[0,0],[0,1]])
D = np.array([[1,2],[0,1]])

x = np.array([2,2])

a = A@x
b = B@x
c = C@x
d = D@x

fig, ax = plt.subplots()

ax.quiver(0, 0, x[0], x[1], angles='xy', scale_units='xy', scale=1, color='b')
ax.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='r')
ax.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='g')
ax.quiver(0, 0, c[0], c[1], angles='xy', scale_units='xy', scale=1, color='k')
ax.quiver(0, 0, d[0], d[1], angles='xy', scale_units='xy', scale=1, color='y')

ax.set_xlim([-8, 8])
ax.set_ylim([-8, 8])

plt.grid()
plt.show()

print('Red    = Ax\nGreen  = Bx\nBlack  = Cx\nYellow = Dx')




