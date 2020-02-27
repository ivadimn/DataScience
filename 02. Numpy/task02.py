# Задание 2
# Вычислите массив a_centered, отняв от значений массива “а”
# средние значения соответствующих признаков, содержащиеся в массиве mean_a.
# Вычисление должно производиться в одно действие. Получившийся массив должен иметь размер 5x2.


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
print(a_centered[:, 1:])
print(a_centered.shape[0])