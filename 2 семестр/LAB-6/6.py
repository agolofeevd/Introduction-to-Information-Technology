import numpy as np

#arr2d = np.array([1, 2, 3, 4, 5, 6])
#print("сортировка:", np.sort(arr2d))
#print("макс индекс:", np.argmax(arr2d))

data = [1, 2, 3, 4, 5, 6]
sorted_data = sorted(data)
max_index = data.index(max(data))
print("сортировка:", sorted_data)
print("макс индекс:", max_index)
