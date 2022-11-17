import person as p
def choice():
    selector = None
    selector = int(input('Введите "1" добавить\n' + \
                         'Введите "2" вывести\n' ))
 
    return selector

while True:
    selector = choice()
    
    if selector == 1:
        p.surname()
        p.name()
        p.number()
        p.null()

    elif selector == 2:
        with open('data.txt') as file:
            for line in file:
                print(line)
                
