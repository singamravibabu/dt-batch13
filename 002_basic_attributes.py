import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2, 3],
                  [4, 5, 6]])

# attributes - shape
print(arr1.shape)
print(arr2.shape)

# attributes - ndim
print(arr1.ndim)
print(arr2.ndim)

# attribute - size
print(arr1.size)
print(arr2.size)

arr3 = np.array((1.0, 2.0, 3.0, 4.0))

# attributes - dtype
print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)
