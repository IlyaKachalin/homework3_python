# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (если получаются длинные числа после запятой, это нормально и особенность данного языка программирования.
# ваш ответ может не совпадать с примером(может получитя 0,20))
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
a = int(input("Введите размерность массива:  "))
list = []
for i in range(a):
    from random import uniform
    f = uniform(-10, 10)
    list.append(round(f, 2))
print(list)

list2 = []
for i in range(a):
    b = list[i]-int(list[i])
    list2.append(round(b, 2))
    i = i+1


list3 = []
for i in range(a):
    if list2[i] < 0:
        b = list2[i]*(-1)
    else:
        b = list2[i]
    list3.append(round(b, 2))

print(max(list3) - min(list3))
