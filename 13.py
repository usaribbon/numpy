import numpy as np
def test(A):
  return np.sum(A,axis=1)

a=np.array([[3, 6, 7, 3, 0, 6],
       [6, 3, 3, 8, 2, 5],
              [4, 2, 4, 5, 3, 0],
                     [3, 3, 5, 3, 3, 3],
                            [2, 1, 3, 1, 4, 0],
                                   [2, 1, 2, 2, 6, 6]])

print(test(a))
