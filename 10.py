import numpy as np
def test(A):
  return A.ravel()
a=np.array([[18, 13,  3, 11,  5],
         [ 0, 18, 12,  0,  8],
                [15, 13, 14,  5,  7],
                       [18,  4,  0,  7, 17],
                              [ 9, 12, 16,  2, 19]])
print(test(a))
