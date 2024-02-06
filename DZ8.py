# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
#    (Например имя или фамилию человека)

# Дополнить справочник возможностью копирования данных из одного файла в другой.
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

# main.py
# FILE_NAME = 'my_phone_book.txt'
from typing import List
def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print('файла нет. Сначала введите данные\n')
        return []

def show_data(data: list):
    for line in data:
        print(line)
    # with open('my_phone_book.txt', 'r', encoding='utf-8') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         print(line)
    # FileNotFoundError
    # try:
    #     # print('открытие файла')
    #     with open('my_phone_book.txt', 'r', encoding='utf-8') as f:
    #         lines = f.readlines()
    #         for line in lines:
    #             print(line)
    # except FileNotFoundError as err:
    #     print('файла нет. Сначала введите данные\n')
    # else:
    #     print('else')
    # finally:
    #     print('finally')

def save_data(file):
    print('Введите данные контакта:')
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{first_name}, {last_name}, {patronymic}, {phone_number}\n')

def search_data(contacts: List[str]):
    # ['Иван, Иванов, Иванович, 123', 'Петр, Иванов, Петрович, 456']
    search_str = input('Введите фамилию для поиска: ')
    founded = []
    # search_idx
    for contact in contacts:
        if search_str.lower() in contact.split(', ')[1].lower():
            founded.append(contact)
    return founded

def copy_line():
    # with open('my_phone_book.txt') as source, open('output.txt', 'w') as destination:
    # for line in source:
    #     if line.strip().endswith('_exec'):
    #         destination.write(line)

def main():
    file_name = 'my_phone_book.txt'
    flag = True
    while flag:
        print('0 - выход')
        print('1 - запись в файл')
        print('2 - показать записи')
        print('3 - найти запись')
        print('4 - скопировать запись в файл')
        answer = input('Выберите действие: ')
        if answer == '0':
            flag = False
        elif answer == '1':
            save_data(file_name)
        elif answer == '2':
            data = read_file(file_name)
            show_data(data)
        elif answer == '3':
            data = read_file(file_name)
            founded_data = search_data(data)
            show_data(founded_data)
        elif answer == '4':



if __name__ == '__main__':
    main()
