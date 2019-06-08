import numpy as np
def test(A):
  return A[:,:3]

a=np.array([[2, 7, 2, 3, 8, 3],
       [6, 1, 4, 6, 3, 3],
              [0, 4, 1, 8, 5, 7],
                     [3, 3, 5, 3, 8, 8],
                            [7, 7, 3, 0, 1, 4],
                                   [3, 5, 8, 6, 1, 8],
                                          [1, 8, 2, 8, 4, 3]])
print(a)
print(test(a))
