import numpy as np

a = np.array([1, 2, 3])

a = np.array([(1,2,3),(4,5,6)])

a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

myList = [1,2,9,8]
a = np.array(myList)

a = np.zeros((2,2))

a = np.ones((3,3))

a = np.array([(1,2,3),(4,5,6)])
a.reshape(3,2)

a = np.array([(1,2,3),(4,5,6)])
b = a.flatten()
b.shape # (6,) NOT (6,1)!

a = np.array([1,2,3,4,5,6,7])
b = np.resize(a, (1,4)) # array([[1, 2, 3, 4]])

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.hstack((a,b))

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.vstack((a,b))

np.arange(start,stop,step) # Numbers from start to stop with a certain step

a = np.arange(1,11,1)

np.linspace(start, stop, num, end) # “num” numbers from start to stop. “end” is a boolean that determines whether to include the stop value.

a = np.linspace(1.0,5.0,10, False)

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a[0] # This gives us the first row of a
a[2] # This gives us the third row of a
a[:,1] # this gives us the second column of a
a[2][2] # this gives us the value of a(2,2), which is 9 here

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
c = a[1] # This gives us the 2nd row of a ([4,5,6])
c[2] = 0 # This assigns the 3rd element to 0 in c, but ALSO in a!
a        # [[1,2,3],[4,5,0],[7,8,9]] – NOTICE THE ZERO!!!

print(array6[0])     # [12 3 1 2]
print(array6[1, 0])  # 0
print(array6[:, 1])  # [3 0 2]
print(array6[2, :2]) # [4 2]
print(array6[2, 2:]) # [3 1] 
print(array6[:, 2])  # [1 1 3]
print(array6[1, 3])  # 2

