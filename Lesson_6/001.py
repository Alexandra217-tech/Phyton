""" Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена 
прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки. """

first_element=int(input("Введите первый элемент: "))
kolvo=int(input("Введите количество элементов: "))
d=int(input("Введите разность: "))
a=[]
an=0
for i in range (1, kolvo):
    an = (first_element + (i-1)) * d
    a.append(an)
print (a)



""" ef new_str ():
     with open('C:\Users\kozub\OneDrive\Рабочий стол\Programm\spravotchnik.txt', 'a') as file:
        file.write(input('Введите новую строку: '+ '\n') )
def delite_inf(inf):
    with open('C:\Users\kozub\OneDrive\Рабочий стол\Programm\spravotchnik.txt', 'a') as file:
        file.write(input('Введите новую строку: '+ '\n') )
file = open ('C:\Users\kozub\OneDrive\Рабочий стол\Programm\spravotchnik.txt', 'r+')
first_name = input("Введите имя: ")
second_name = input("Введите фамилию: ")
number = input("Введите номер телефона")


while True:
    a = input ("Для того чтобы добавить новую строку в формате имя+фамилия+номер телефона введите цифру "1"; чтобы удалить данные - "2"; изменить данные - "3"; вывести - "4" : ")
    if a == "1":
        new_str()
if a == "2": """ 
