import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5,6,1)#change area here
y = np.arange(-5,6,1)#change area here

X, Y = np.meshgrid(x,y)

t = 1  #change here  for time t
Z = 1  #change here for layer Z
u = 3*t  #If you need to change function u
v = -X*Z   #If you need to change function 
v  
fig, ax  = plt.subplots(figsize=
(7,7))
ax.quiver(X,Y,u,v)

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.axis([-6, 6, -6, 6])
ax.set_aspect('equal')

plt.show()

