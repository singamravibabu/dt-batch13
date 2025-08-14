import numpy as np

arr = np.arange(1, 21).reshape(4, 5)
print(arr)

print(arr[0])
print(arr[0, ])
print(arr[1, 2])
print(arr[1, 2:4])
