import numpy as np

array_a = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3]])
array_b = np.array([0,1,2,3])
array_c = np.array([[1],[2],[3]])
array_d = np.array([[0,1,2,3],[0,1,2,3],[0,1,2,3]])


# for broadcasting to work, the two arrays have to have at least 
# one dimension in common
print(array_a + array_b)
print(array_a + array_d)

# project



array = np.array([[1,2,3],[4,5,6],[7,8,9]])
array_1 = np.array([3,2,1])
array_2 = np.array([[3],[2],[1]])
print(array)
print(array + array_1)
print(array + array_2)


#challenge
array_5x5 = np.ones((5,5))
array_1x5 = np.array([1,2,3,4,5])
print(array_1x5 * array_5x5)