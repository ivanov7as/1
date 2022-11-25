import csv
import os.path
import view

def find_element():
    str = input('ВВедите необходимые данные для поиска: ')
    with open("data.csv", 'r' , encoding='utf-8' ) as file:
        lines = file.readlines()

    for line in lines:
        if str in line:
            print(line)
