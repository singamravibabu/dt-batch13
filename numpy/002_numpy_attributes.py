import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr4 = np.array([[1., 2., 3., 4.],
                 [5., 6., 7., 8.],
                 [9., 10., 11., 12.],
                 [13., 14., 15., 16.],
                 [17., 18., 19., 20.]])


print("Array 1:")
print("Shape:", arr1.shape)
print("Dimensions:", arr1.ndim)
print("Size:", arr1.size)
print("Data type:", arr1.dtype)
print()
print("Array 2:")
print("Shape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Size:", arr2.size)
print("Data type:", arr2.dtype)
print()
print("Array 3:")
print("Shape:", arr3.shape)
print("Dimensions:", arr3.ndim)
print("Size:", arr3.size)
print("Data type:", arr3.dtype)
print()
print("Array 4:")
print("Shape:", arr4.shape)
print("Dimensions:", arr4.ndim)
print("Size:", arr4.size)
print("Data type:", arr4.dtype)