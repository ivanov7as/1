import os.path
import csv


def record_data():
    if not os.path.exists('data.csv'):
        with open('data.csv', 'w', encoding='utf-8') as dt:
            writer = csv.writer(dt, delimiter=';')
            writer.writerow(('surname', 'name', 'name2', 'occupation'))
    exit = ''
    while exit != 'q':
        users_data = [
            [input('введите фамилию: '), input('введите имя: '), input('отчество: '), input('должность: ')]
        ]
        with open('data.csv', 'a', encoding='utf-8') as dt:
            writer=csv.writer(dt, delimiter = ';')
            writer.writerow(
                users_data
            )
        exit = input('Для завершения ввода данных нажмите "q"\nДля продолжения нажмите"Enter"\n')
