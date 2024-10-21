import numpy as np

array1 = np.array([3,7,4,9,1,6,5,4,3,4,7,4,2,4,1,4]) 
array_unicos, conteos = np.unique(array1, return_counts=True)
conteos_ord = np.argsort(conteos)

print(array_unicos[conteos_ord[-1]])