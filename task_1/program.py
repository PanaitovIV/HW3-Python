# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.

import random

n = int(input("Введите количество элементов массива > "))
arr = [random.randint(1, 9) for i in range(n)]
print(arr)
x = int(input('Введите число X > '))
count = 0
for i in arr:
    if i == x:
        count += 1
print(f"Число {x} встречается в данном массиве {count} раз(а)")