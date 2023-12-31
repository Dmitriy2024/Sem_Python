#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих 
#наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов
# второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint
n = int(input('Введите кол-во элементов первого множества '))
m = int(input('Введите кол-во элементов второго множества '))


numbres_n = set(randint(1, 30) for i in range(int(n)))
print(numbres_n)

numbers_m = set(randint(1, 30) for i in range(int(m)))
print(numbers_m)

numbers = sorted(numbres_n.intersection(numbers_m))
print(*numbers)


#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два 
#соседних. Всего на грядке растёт N кустов.
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное
# число ягод — на i-ом кусте выросло ai ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система
# состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один
# заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с 
#двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может собрать за один
# заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# import random
# bush = int(input("введите количество кустов: "))
# berryes = list(random.randint(3, 10) for i in range(bush))
# result = []
# i = 0
# sum = 0

# print(berryes)

# while (i < bush):
#     if (i == bush - 1):
#         sum = berryes[i] + berryes[i - 1] + berryes[0]
#     else:
#         sum = berryes[i] + berryes[i - 1] + berryes[i + 1]
#         result.append(sum)
#         result.sort()
#     i += 1

# print(f"максимальное число ягод за одн  {result[-1]}")