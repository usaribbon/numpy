import numpy as np
def test(A):
    return A.ravel(order='F')


a=np.array([[ 1,  2,  4],
       [ 0, 12,  9],
       [ 5, 17, 12],
       [13, 17, 15],
       [11,  1, 15]])
#print(test(a))

print(a.T)
b = a.T.reshape((15,))
print b
