import numpy as np


array_a = np.array([1,2,3,4,5])
print(array_a)

print(array_a.shape)

array_b = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
print(array_b.shape)

seq_a = [1,2,3]
seq_b = [4,5,6]
seq_c = [7,8,9]
seq_d = [10.5,11.5,12.5]

array_abc = np.array([seq_a, seq_b, seq_c])
print(array_abc.shape)

array_d = np.array([[1,1],[2,2],[3,3],[4,4],[5,5]])
print(array_d.shape)


