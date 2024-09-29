import numpy as np


my_array = np.arange(1,10).reshape((3,3))
my_transp = my_array.transpose(1,0)



print(my_array)
print()
print(my_transp)

