import numpy as np
def test(A):
  return A.all()
a=np.array([[1, 5, 4, 7],
       [2, 3, 1, 5],
              [5, 4, 2, 2]])

print(test(a))
