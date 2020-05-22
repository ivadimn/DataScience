import numpy as np

a = np.zeros((2, 2))
print(a)
b = np.ones((3, 2))
print(b)

ab = np.vstack((a, b))
print(ab)
abt = ab.transpose()
print(abt)

a = np.random.normal(8, 1, 16)
print(a)