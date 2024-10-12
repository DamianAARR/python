import numpy as np

array_aleatorio = np.random.randint(1,100, size=(15))

multi1 = 1

for i in range(0,len(array_aleatorio)):
    multi1 *= array_aleatorio[i]
print(multi1)