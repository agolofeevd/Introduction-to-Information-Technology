import numpy as np

arr2d = np.array([[1, 2, 3], [4, 5, 6]])

print("сумма в строка (axis=1):", arr2d.sum(axis=1))
print("ср.знач в столбцах (axis=0):", arr2d.mean(axis=0))