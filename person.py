def surname():
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write("Фамилия "+input('введите фамилию ')+'\n')
def name():
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write("Имя "+input('введите имя ')+'\n')
def number():
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write("Номер "+input('введите номер ')+'\n')
def null():
    with open('data.txt', 'a') as file:
        file.write("****************"+'\n')
