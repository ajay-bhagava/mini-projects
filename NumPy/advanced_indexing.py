import numpy as np

row_1 = [1,2,3,4,5] 
row_2 = [6,7,8,9,10]
row_3 = [11,12,13,14,15]
row_4 = [16,17,18,19,20]
row_5 = [21,22,23,24,25]

test_data = np.array([row_1,row_2,row_3, row_4, row_5])
print(test_data)

# slice 
print(test_data[:,2:4:1])
# negative index
print(test_data[:,-2:-4:-1])

# boolean indexing
greater_than_five = test_data > 5
print(greater_than_five)
# this prints a one dimensional array with only the trues in greater_than_five
print(test_data[greater_than_five])

# where
# allows boolean indexing to return multidimensional arrays
# will turn anything that doesnt meet the condition into 0
drop_under_5_array = np.where(test_data > 5, test_data, 0)
print(drop_under_5_array)

# logical_and so that we can a boolean matric using multiple conditions
drop_under_5_and_over_20 = np.logical_and(test_data > 5, test_data < 20)
print(drop_under_5_and_over_20)
# another one dimesntional array
print(test_data[drop_under_5_and_over_20])



# Practice
array_a = np.arange(0,100,5)
print(array_a)
print(array_a.size)

array_a_reshape = array_a.reshape(4, 5)
print(array_a_reshape)

#negative index
print(array_a_reshape[:,-1])

#boolean indexing
array_a_above_50 = array_a_reshape[array_a_reshape > 50]
print(array_a_above_50)

# python slice
print(array_a_above_50[0::2])

# slice of a row
# for every row, print every other element in that row
print(array_a_reshape[:, 0::2])

# more where
print(np.where(array_a_reshape > 50, array_a_reshape * 2, -1))

# challange: reverse every row using negative indexing
print(array_a_reshape[:, -1:-4:-1])

# chalenge: keep shape but only keep values between 25 and 75
print(np.where(np.logical_and(array_a_reshape >= 25, array_a_reshape < 75), array_a_reshape, -1))