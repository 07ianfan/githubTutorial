import numpy as np

my_matrix = np.identity(4)
print(my_matrix)

def my_function(matrix_1, matrix_2):
	try:
		return matrix_1 * matrix_2
	except ValueError:
		return None

my_matrix = np.identity(4)
my_2nd_matrix = np.random.random(size =(4,5))

print(my_function(my_matrix, my_2nd_matrix))