https://docs.python.org/3/library/csv.html

https://docs-python.ru/standart-library/modul-csv-python/priemy-raboty-modulem-csv/  
https://docs-python.ru/standart-library/modul-csv-python/klass-dictreader-modulja-csv/
https://docs.python.org/3/library/json.html
https://docs-python.ru/standart-library/modul-json-python/priemy-raboty-modulem-json/
https://docs.python.org/3/library/sqlite3.html
https://docs-python.ru/standart-library/modul-sqlite3-python/brief-description/

# main.py
# FILE_NAME = 'phone_book.txt'
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
    # with open('phone_book.txt', 'r', encoding='utf-8') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         print(line)
    # FileNotFoundError
    # try:
    #     # print('открытие файла')
    #     with open('phone_book.txt', 'r', encoding='utf-8') as f:
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

def main():
    file_name = 'phone_book.txt'
    flag = True
    while flag:
        print('0 - выход')
        print('1 - запись в файл')
        print('2 - показать записи')
        print('3 - найти запись')
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

if __name__ == '__main__':
    main()

22:14
import csv

list_contacts = [{'last_name': 'Иванов', 'first_name': 'Иван', 'patronymic': 'Иванович', 'phone_number': '123',},
                 {'last_name': 'Петров', 'first_name': 'Иван', 'patronymic': 'Сергеевич', 'phone_number': '555',}]

with open('examle_file.csv', 'w', newline='', encoding='utf-8') as csv_file:
    # fieldnames = ['last_name', 'first_name', 'patronymic', 'phone_number']
    fieldnames = list_contacts[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(list_contacts)