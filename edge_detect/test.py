import numpy as np

arr = [ [5, 7, 9, 11, 13], 
        [15, 17, 19, 21, 23]]
arr = np.array(arr)
#print(arr%3 == 0)
arr[arr < 10] = 0
arr[arr > 10] = 1
print(arr)