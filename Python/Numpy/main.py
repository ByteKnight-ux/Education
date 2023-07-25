import numpy as np

# CREATION OF NORMAL ARRAYS WITH N-DIMENTIONS
a = np.array([(1,2,3,4,5),[6,7,8,9,10],[11,12,13,14,15]])
print(a.ndim, a.shape, a.dtype, a.size, sep=', ', end='\n\n')
a.sort()
print(a, end='\n\n')

# a = np.random.random_integers(1,20, 5)  # DEPRECATED
a = np.random.randint(1,21)
print(a, end='\n\n')

# DEFAULTS TO FLOAT DATATYPE
a = np.zeros((3,5), dtype='int64')
print(a, end='\n\n')

# DEFAULTS TO FLOAT DATATYPE
a = np.ones((3,5), dtype='int64')
print(a, end='\n\n')

# FILLS THE ARRAY WITH RANDOM VALUES WHICH IS TO BE FILLED LATER BY OURSELVES
a = np.empty((2,2))
print(a, end='\n\n')

# MAKES THE ARRAY FROM 1 TO 15 SHAPE (1, ) AND THEN RESHAPES IT TO SHAPE(3, 5)
a = np.arange(1, 16).reshape(3,5)
print(a, end='\n\n')

# PERFORMING MATHEMATICAL OPERATIONS BETWEEN NUMPY ARRAYS
a = np.arange(1,3)
b = np.arange(3,5)[::-1]
# ADDITION
print(a+b)
# SUBTRACTION
print(b-a)
# MULTIPLICATION
print(a*b)
# QUOTIENT
print(b/a)
# MATRIX PRODUCT
print(a@b)
print(a.dot(b), end='\n\n')     # ALTERNATIVE

# PERFORMING MATHEMATICAL OPERATIONS USING CONSTANTS
a = np.arange(5)
print(a*3, end='\n\n')

# AXIS = 0:COLUMN, 1:ROW
a = np.arange(1,16).reshape(3,5)
# 0: SUM OF THE COLUMNS, 1: SUM OF THE ROWS
print(a.sum(axis=0), a.sum(axis=1), end='\n\n')

# UNIVERSAL FUNCTIONS IN NUMPY
a = np.arange(1,16).reshape(3,5)
# NEW ARRAY WITH SQUARE ROOT OF EACH ELEMENT
print(np.sqrt(a), end='\n\n')

# DIFFERENCE BETWEEN RESHAPE() AND RESIZE()
a= np.arange(1,17)
print(a, end='\n\n')
# RESHAPE RETURNS THE SHAPE MODIFIED ARRAY
m = a.reshape((8,2))
print(m, end='\n\n')
# RESIZE MODIFIES THE ORIGINAL ARRAY ITSELF
a.resize((8,2))
print(a, end='\n\n')
# -1 WILL MAKE IT CALCULATE THE OTHER DIMENSION AUTOMATICALLY
m2 = a.reshape(4,-1)
print(m2, end='\n\n')

a = np.arange(2,21,2).reshape(5,2)
print(a)
# RETURNS A MATRIX OF THE MAXIMA INDEX FOR EACH SERIES
print(a.argmax(axis=1))
# RETURNS A MATRIX OF THE MINIMA INDEX FOR EACH SERIES
print(a.argmin(axis=0))