#!/usr/bin/python3

import numpy as np
#  NumPy provides an array that can have N-dimensions. NumPy serves as the base for many packages that can extend its capabilities, such as, pandas and scikit-learn

# We can use numpy to create an array
var_numpy_array = np.arange(10)
print(var_numpy_array)

var_numpy_float_array = np.arange(10, dtype=float)
print(var_numpy_float_array)

# complex array
var_numpy_complex_array = var_numpy_float_array.astype(complex)
print(var_numpy_complex_array)

# Turning a list into an array
var_numpy_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(var_numpy_list)
var_numpy_int_array = np.array(var_numpy_list)
print(var_numpy_int_array)

# Lets import data from a csv file and create an array from it.

var_numpy_csv = np.genfromtxt('../Data Files/numpy.csv', dtype='int', delimiter=',')
print(var_numpy_csv)
# lets get the 3rd - 10th values in the array.
print(var_numpy_csv[2:9])

# lets create a matrix

