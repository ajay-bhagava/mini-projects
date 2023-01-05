import numpy as np

array_a = np.array([[1,2],[3,4]])
array_b = np.array([[2,2],[6,6]])

# single array operations
print(array_a.sum(axis=1))
print(array_a.cumsum())
print(array_a.prod())
print(array_a.cumprod())

# two array math
# these just run the operation on corresponding elements of the arrays
print(array_a + array_b)
print(array_a - array_b)
print(array_a * array_b)
print(array_a / array_b)

# dot product
print(np.dot(array_a, array_b))

# power, uses element from first array as base,
# corresponding element from second as exponent
print(np.power(array_b, array_a))