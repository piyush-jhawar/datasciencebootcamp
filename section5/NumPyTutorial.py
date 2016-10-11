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

#4 NumPy Array Indexing and Selecting.
arr = np.arange(0,11)
print(arr)
print(arr[8])
print(arr[1:5])
print(arr[:6])
print(arr[5:])
# arr[0:5] = 100
slice_of_arr = arr[0:6]
print(slice_of_arr)
slice_of_arr[:] = 99
print(arr)
arr_copy = arr.copy()
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)
print(arr_2d[0][0])
print(arr_2d[1][1])
print(arr_2d[1,2])
print(arr_2d[:2,1:])
arr = np.arange(1,11)
print(arr)
print(arr > 5)
print(arr[arr<3])

#5 NumPy Operations
arr = np.arange(0,11)
print(arr)
print(arr+arr)
print(arr + 2)
#universal array function
print(np.sqrt(arr))
print(np.exp(arr))
print(np.max())
print(np.sin(arr))
print()


