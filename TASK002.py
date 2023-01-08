# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
a = int(input("Введите размерность массива:  "))
list = []
for i in range(a):
    from random import randint
    list.append(randint(-10, 10))

print(list)

list2 = []
for i in range(len(list)):
    while i < len(list)/2 and a > len(list)/2:
        a = a - 1
        c = list[i] * list[a]
        list2.append(c)
        i += 1
print(list2)
