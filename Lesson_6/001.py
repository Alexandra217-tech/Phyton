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