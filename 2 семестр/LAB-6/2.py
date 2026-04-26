import numpy as np

arr1d = np.array([1, 2, 3, 4, 5])

print("cумма:", arr1d.sum())
print("cр.знач:", arr1d.mean())
print("min:", arr1d.min())
print("max:", arr1d.max())
print("отклонение:", arr1d.std())

arr2d = np.array([1, 2, 3, 4, 5])

print("сложение:", arr1d + arr2d)
print("умножение:", arr1d * arr2d)
