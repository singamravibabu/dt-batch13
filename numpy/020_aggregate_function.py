import numpy as np

arr = np.array([[1, 2, 3],
               [4, 5, 6]])
print(np.sum(arr))  # Sum of all elements
print(np.sum(arr, axis=0))  # Sum along columns
print(np.sum(arr, axis=1))  # Sum along rows

print(np.mean(arr))  # Mean of all elements
print(np.min(arr))   # Minimum of all elements
print(np.max(arr))  # Minimum and maximum of all elements
print(np.std(arr))  # Standard deviation of all elements
