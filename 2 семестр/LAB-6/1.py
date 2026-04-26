import numpy as np

arr1d = np.array([1, 2, 3, 4, 5])
print("одноменрный:", arr1d)
print("размерность (ndim):", arr1d.ndim)
print("форма (shape):", arr1d.shape)
print("тип данных (dtype):", arr1d.dtype)
print("колво. элементов (size):", arr1d.size)

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("двумерный:", arr2d)
print("размерность (ndim):", arr2d.ndim)
print("форма (shape):", arr2d.shape)
print("тип данных (dtype):", arr2d.dtype)
print("колво. элементов (size):", arr2d.size)

print("лемент arr2d[0, 2]:", arr2d[0, 2])
print("первая строка arr2d[0, :]:", arr2d[0, :])
print("второй столбец arr2d[:, 1]:", arr2d[:, 1])
print("срезы по строкам и столбцам arr2d[:2, :2]:", arr2d[:2, :2])