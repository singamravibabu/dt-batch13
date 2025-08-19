import numpy as np

arr = np.array([1, 2, 3])
arr2d = arr[np.newaxis, :]
print(arr2d)
arr2d_new = arr[:, np.newaxis]
print(arr2d_new)
