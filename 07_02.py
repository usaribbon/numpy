
import numpy as np

a = np.array([8, 3, 2, 1, 2])
print a
b = np.concatenate([a[-1:], a[:-1]])
print b
