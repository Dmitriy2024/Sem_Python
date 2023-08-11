#Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
 #разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
#Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может
# состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу 
#с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и
# “Пам парам”, если с ритмом все не в порядке.

# пара-ра-рам рам-пам-папам па-ра-па-да
# пара-ру-ром рым-пим-пэпюм пя-рё-пе-да

poems = input('Введите стих ')
print(poems)
poems = poems.split(' ')

print(poems)
print(len(poems))
list_1 = []

for i in range(len(poems)):
    checksum = 0
    letter = poems[i] 
    for i in range(len(letter)):
       if letter[i] == 'а' :
        checksum+=1
       elif letter[i] =='е':
          checksum+=1  
       elif letter[i] =='ё':
          checksum+=1  
       elif letter[i] =='и':
           checksum+=1
       elif letter[i] =='о':
          checksum+=1     
       elif letter[i] =='у':
          checksum+=1  
       elif letter[i] =='ы':
          checksum+=1    
       elif letter[i] =='э':
          checksum+=1     
       elif letter[i] =='ю':
          checksum+=1  
       elif letter[i] =='я':
          checksum+=1   
    list_1.append(checksum)            

checksum_1=0

for i in range(len(list_1)):
   if list_1[0] != list_1[i]:  
      print(f' i {i}')
      checksum_1+=1
if checksum_1 == 0:      
   print('Парам пам-пам')
else:
   print('Пам парам')   


#Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки
 #и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, 
#у которой ровно два аргумента, как, например, у операции умножения.
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     l = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in l:
#         print(*[f"{x:>3}" for x in i])
# print_operation_table(lambda x, y: x * y)




