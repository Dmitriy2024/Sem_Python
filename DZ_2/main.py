#Задача 10.На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые –
# гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все
# монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть

# import random
# n =int(input("Введите кол-во монет "))
# i =  1
# man1 = 0
# man2 = 0
# for i in range(n):
#     temp = random.randint(0, 1)
#     print(temp, end='' )
#     if temp > 0:
#         man1 = man1 + 1
#     else:
#         man2 = man2 + 1
# if man1 > man2:
#             print(f" -> {man2}")
# else:
#             print (f" -> {man1}")    


#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает
# Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна 
#их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# S = int(input("Введите сумму чисел ")) 
# P = int(input("Введите произведение "))
# n = 1001

# for i in range(n):
#   for j in range(n):
#    if (i + j) == S and (i * j) == P:
#      print(f"Первое число {i}, второе число {j}")   

     
 # 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие
#числа N.      
# N = int(input("Введите число N  "))

# for i in range(N):
#     degree = 2 ** i
#     print(degree, end=" " )