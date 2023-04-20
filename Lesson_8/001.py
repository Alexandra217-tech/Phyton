""" Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
для изменения и удаления данных. """




def information():
    with open(r'C:\Users\kozub\OneDrive\Рабочий стол\Programm\spravotchnik.txt', 'r') as file:
        txt = file.read()
    return txt

def new_information():
        with open(r'C:\Users\kozub\OneDrive\Рабочий стол\Programm\spravotchnik.txt', 'a') as file:
            file.write(input('Введите новую строку: '+ '\n') )
    
def find_information():
    with open(r'C:\Users\kozub\OneDrive\Рабочий стол\Programm\spravotchnik.txt', 'r') as file:
        txt = file.read().split('\n')
        a = input('что ищем?: ')
        for i in txt:
            if a in i:
                print(i)

def delete_information(name):
    """Удаляет данные"""
    persons = information()
    with open(r"C:\Users\kozub\OneDrive\Рабочий стол\Programm\spravotchnik.txt", "w") as file:
        for person in persons:
            if name != person:
                file.write(person)

def change_information (new_name, old_name):
    persons = information()
    with open(r"C:\Users\kozub\OneDrive\Рабочий стол\Programm\spravotchnik.txt", "w") as file:
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")

while True:
    mode = input('Для того чтобы добавить новую строку в формате имя+фамилия+номер телефона введите цифру "1"; ' + '\n'
                  +'чтобы удалить данные - "2"; изменить данные - "3"; вывести - "4"; найти - "5"; закрыть -"6" : ')

    if mode == '1':
        new_information()
    elif mode == '2':
        name = input('Кого хотите удалить?: ')
        delete_information(name)
    elif mode == '3':
        old_name = input('Кого желаете переименовать? ')
        new_name = input('На какое имя меняем?: ')
        change_information (new_name,old_name)
    elif mode == '4':
        print(information())
    elif mode == '5':
        find_information()
    elif mode == '6':
        break
    else:
        print('do not understand ')