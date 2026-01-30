import numpy as np


array = np.random.randint(0,20,12).reshape(3,4)
print(array)
print("-------------")
novo = array.copy()

for i in array.flat:
    if i <=0:
        novo[i]= 0





