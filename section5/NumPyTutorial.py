import numpy as np
from numpy.random import randn

#1 Introduction to NumPy
#2 NumPy Arrays

list = [1,2,3,4]
print(np.array(list))

my_mat = [[1,2,3],[4,5,6],[7,8,9]]
print(np.array(my_mat))


#common way

print(np.arange(0,10,2))
print(np.zeros((5,5)))
print(np.ones((3,4)))
print(np.linspace(0,5,10))
print(np.eye(4))
print(np.random.rand(5,5))
print(np.random.randn(5,5))
arr = np.arange(25)
print(arr)
ranarr = np.random.randint(0,50,10)
print(ranarr)
print(arr.reshape(5,5))
print(ranarr.max())
print(ranarr.min())
print(ranarr.argmax())
print(ranarr.argmin())
print(arr.shape)
print(arr.dtype)
print(randn(5,2))