import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
x = np.arange(0,100)
y = x*2
z = x**2

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)

fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.2,.2])
ax1.plot(x,y,'r')
ax2.plot(x,y,'r')

fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.4,.4])
ax1.plot(x,z)
ax1.set_xlabel('X')
ax1.set_ylabel('Z')
ax2.plot(x,y)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_xlim([20,22])
ax2.set_ylim([30,50])
plt.show()