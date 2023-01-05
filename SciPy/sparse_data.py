import numpy as np
from scipy.sparse import csr_matrix

# CSC - Compressed Sparse Column. For efficient arithmetic, fast column slicing.
# CSR - Compressed Sparse Row. For fast row slicing, faster matrix vector products

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2]) 

# print(csr_matrix(arr))

arr2 = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]]) 
print(csr_matrix(arr2).data)
