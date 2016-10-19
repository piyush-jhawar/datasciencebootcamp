import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline only for jupyter notebook

#3 Matplotlib Part1
#Matplotlib Concepts Lecture

x = np.linspace(0,5,11)
y = x ** 2

#Functional
plt.plot(x,y)
plt.xlabel("X Lab")
plt.ylabel("Y Lab")
plt.title("Title")
plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(y,x,'b')
#Object Oriented Method is the best way
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('Xlab')
axes.set_ylabel('Ylab')
axes.set_title('Title')
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
axes1.plot(x,y)
axes2.plot(y,x,'r')

#4 Matplotlib Part2
#Lecture40
fig,axes = plt.subplots(nrows=1,ncols=2)
# plt.tight_layout()
axes[0].plot(x,y)

# fig = plt.figure(figsize=(6,6),dpi=100)
#
# ax = fig.add_axes([0,0,1,1])
# ax.plot(x,y)
# ax.plot(y,x)

#save a figure
# fig.savefig('my_fig.png')
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2,label='X2')
ax.plot(x,x**3,label='X3')
ax.legend(loc=0)


#5 Matplotlib Part3
#Lecture41
#Plot appearence
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
# ax.plot(x,y,color='green',linewidth=3,alpha=0.7,
#         linestyle='-',marker='o',markersize=20,
#         markerfacecolor='yellow',
#         markeredgewidth=3,
#         markeredgecolor='blue') #hex code
ax.plot(x,y,color='green',linewidth=3,alpha=0.7,
        linestyle='-')
ax.set_xlim([0,1])
ax.set_ylim([0,2])


plt.show()



