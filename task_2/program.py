# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.

import random
n = int(input("Введите количество элементов массива > "))
arr = [random.randint(1, 10) for i in range(n)]
print(arr)
x = int(input("Введите число X > "))
res = arr[0]
for i in range(n):
    if abs(arr[i] - x) < abs(res - x):
        res = arr[i]
print(f"В массиве {arr} к числу {x} ближайшее число - {res}")      