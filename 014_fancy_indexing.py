import numpy as np
arr = np.array([10, 20, 30, 40, 50])
indices = [1, 3, 4]
print(arr[indices])  # output: [20 40 50]

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print(arr2d[[0, 2], [1, 2]])  # output: [2 9]
