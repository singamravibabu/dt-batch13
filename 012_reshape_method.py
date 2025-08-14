import numpy as np

arr = np.arange(12)
print(arr)

arr1 = arr.reshape(2, 6)
print(arr1)

arr2 = arr.reshape(3, 4)
print(arr2)

arr3 = arr.reshape(4, 3)
print(arr3)

arr4 = arr.reshape(6, 2)
print(arr4)

arr5 = arr.reshape(12, 1)
print(arr5)