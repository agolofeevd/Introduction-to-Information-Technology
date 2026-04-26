import numpy as np

arr2d_int = np.array([1, 2, 3, 4, 5, 6], dtype=np.int32)
arr2d_float = arr2d_int.astype(np.float64)

print("int32 памяти:", arr2d_int.nbytes)
print("float64 памяти:", arr2d_float.nbytes)