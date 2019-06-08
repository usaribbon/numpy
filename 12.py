import numpy as np
def test(A,B):
  return np.concatenate([A,B])

a=np.array([[4, 8, 2, 5, 5],
       [4, 8, 3, 6, 6],
              [3, 2, 6, 3, 7],
                     [0, 0, 2, 1, 2]])

b=np.array([[6, 6, 3, 1, 0],
       [8, 7, 5, 1, 7],
              [8, 8, 4, 2, 4],
                     [0, 2, 8, 6, 1]])

print(test(a,b))
