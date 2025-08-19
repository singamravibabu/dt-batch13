import numpy as np

# old way doing
arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([1])
arr3 = np.array([[1], [2]])
arr4 = np.array([[1], [2], [3]])
arr5 = np.array([[1], [2], [3], [4]])
print(arr1 + arr2)  # Broadcasting addition
print(arr1 + arr3)  # Broadcasting addition
print(arr1 + arr4)  # Broadcasting addition
print(arr1 + arr5)  # Broadcasting addition