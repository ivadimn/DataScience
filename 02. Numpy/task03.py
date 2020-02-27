# Задание 3
# Найдите скалярное произведение столбцов массива a_centered.
# В результате должна получиться величина a_centered_sp.
# Затем поделите a_centered_sp на N-1, где N - число наблюдений.


import numpy as np

a = np.array([[1, 6],
             [2, 8],
             [3, 11],
             [3, 10],
             [1, 7]])

mean_a = np.mean(a, axis=0)
print(mean_a)
print("*" * 40)
a_centered = a - mean_a
print(a_centered)
print("*" * 40)

al = a_centered[:, :1].flatten()
ar = a_centered[:, 1:].flatten()
print(al)
print(ar)
print("*" * 40)
a_centered_sp = np.dot(al, ar) / (a.shape[0] - 1)
print(a_centered_sp)
