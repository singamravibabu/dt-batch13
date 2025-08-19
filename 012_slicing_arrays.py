import numpy as np
arr = np.array([10, 20, 30, 40, 50])
arr2d = np.array([[1, 2, 3],
                  [4, 5, 7],
                  [7, 8, 9]])

print(arr[1:4])  # output: [20 30 40]
print(arr[:3])   # output: [10 20 30]
print(arr[::2])  # output: [10 30 50]

print(arr2d[0:2, 0:2])  # output: [[1 2] 
                        #          [4 5]]
print(arr2d[:, 0]) # output: [1 4 7]