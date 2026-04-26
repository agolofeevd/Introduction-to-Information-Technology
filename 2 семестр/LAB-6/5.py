import numpy as np

#arr2d = np.array([[1, 2, 3], [4, 5, 6]])

#маска = arr2d > 3
#print("маска:", маска)
##print("фильтрация:", arr2d[маска])


data = [[1,2,3],[4,5,6]]
фильтрация = []
for row in data:
    for elem in row:
        if elem > 3:
            фильтрация.append(elem)
print("Без NumPy фильтрация:", фильтрация)