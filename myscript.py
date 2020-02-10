import numpy as np
import pandas as pd


my_matrix = np.identity(4)
print(my_matrix)

def my_function(matrix_1, matrix_2):
	try:
		return matrix_1 * matrix_2
	except ValueError:
		print("matrixies are not aligned")
		return None

my_matrix = np.identity(5)
my_2nd_matrix = np.random.random(size =(5,4))

print(my_matrix.dot(my_second_matrix))