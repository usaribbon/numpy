import numpy as np
def test(A):
  return np.where(a < 8,0,A)
a=np.array([[17, 18, 19,  5, 17,  4, 18,  1, 14],
       [ 1,  9, 14,  7,  9,  4, 19, 11, 17],
              [18,  7,  1,  5, 12, 10,  8,  1,  6],
                     [10,  5,  7,  4, 12, 17,  2, 11, 10],
                            [ 7,  3, 11, 13, 18, 17, 19,  6,  7],
                                   [ 1,  4, 16, 18, 10,  4, 11, 12, 18],
                                          [14,  2, 17,  6,  3, 15, 11, 10, 19],
                                                 [ 8,  8,  6, 14, 16,  5,  1,  3,  7],
                                                        [17,  2,  3, 11, 14, 15,  3,  3, 19]])


#print(test(a))

a[a <= 8] = 0.
print a
