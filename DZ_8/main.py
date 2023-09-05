# # Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# # Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных.
action = None
file_path = 'file.txt'

def open_book():
   with open(file_path, 'r', encoding='UTF-8') as file:
                phone = file.read()
                print(phone )          

def add_contact():
  phone = []
  phone=input("Введите имя и номер, через ';'").split('; ')
  data = open(file_path, 'a', encoding='UTF-8') 
  data.writelines(phone)
  data.writelines('\n')
  data.close
  print(f"Контакт {phone[0]} добавлен")  

def find_contact():
  phone_book = []
  name = input('Введите име контакта: ')
  with open(file_path, 'r', encoding='UTF-8') as file:
         phone_book = file.read()
         print(phone_book)
         # for name in phone_book: 
           
         #   if name == phone_book:
              
         #      print(f'> Такой номер есть  <')
         #   else:
         #      print('Нет такого контакта')     
              
              
                       
             

while action != 0:
     print('Телефонный справочик')
     action = int(input('Выберете действия и введите номер действия:\n 1-Посмотреть справочник. \n 2-Создать контакт. \n 3-Найти контакт. \n 4-Редактировать контакт \n 5-Удалить контакт. \n 0-Выйти из справочника. '))     
     if action == 1:
              open_book() 
     elif action == 2:
      
      add_contact()
     elif action == 3:
         find_contact()
          
         

     elif action == '4':
       print('4')



                       
             
