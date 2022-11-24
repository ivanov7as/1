import csv
def id():
    with open('data.csv', 'a', encoding='utf-8') as file:
        file.write("ID "+input('введите ID ')+'\n')
def surname():
    with open('data.csv', 'a', encoding='utf-8') as file:
        file.write("Фамилия "+input('введите фамилию ')+'\n')
def name():
    with open('data.csv', 'a', encoding='utf-8') as file:
        file.write("Имя "+input('введите имя ')+'\n')
def number():
    with open('data.csv', 'a', encoding='utf-8') as file:
        file.write("Номер "+input('введите номер ')+'\n')
def age():
    with open('data.csv', 'a', encoding='utf-8') as file:
        file.write("Возраст "+input('введите возраст ')+'\n')
def work():
    with open('data.csv', 'a', encoding='utf-8') as file:
        file.write("Должность "+input('введите должность ')+'\n')
def null():
    with open('data.csv', 'a', encoding='utf-8') as file:
        file.write(""+'\n')

