import numpy as np

array_a = np.array([[1,2,3],[4,5,6]])
print(array_a.size)
print(array_a.shape)

array_b = array_a.reshape(3,2)
print(array_b)

# print rows and columns
# row
print(array_a[0])

# column
print(array_a[:,2])

# Practice
array_a1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

# reshaping
array_b1 = array_a1.reshape(2,8)
print(array_b1)

#double Trnspose
array_c1 = array_a1.T
print(array_c1.T)

print(array_c1[0], array_c1[1])
print(array_a1[:,-3])
print(array_a1[2,-3])