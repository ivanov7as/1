symbol=(input('введите текст '))
print(symbol)
symbol=list(symbol)
a='а'
b='б'
c='в'
for i in range(0, len(symbol)-3):
    if symbol[i]==a and symbol[i+1]==b and symbol[i+2]==c:
        del symbol[i]
        symbol.append("")
        del symbol[i]
        symbol.append("")
        del symbol[i]
        symbol.append("")
symbol=''.join(symbol)
print(symbol)

from random import randint
numberofcandys=2021
generator = int(input('введите порядок первого хода 1-игрок;2-компьютер '))
if generator !=1 and generator!=2:
    print('неверно')
    generator = int(input('введите порядок первого хода 1-игрок;2-компьютер '))
if generator == 1:
    print('всего конфет', numberofcandys)
    print('Первым ходит игрок')
    playercandys=int(input('введите число от 1 до 28 '))
    if playercandys > 28:
        print ('неверно, повторите ввод')
        playercandys=int(input('введите число от 1 до 28 '))
    numberofcandys-=playercandys
    print('конфет осталось', numberofcandys)
    while numberofcandys>86:
            print ('ход компьютера')
            numberofcandys=numberofcandys-28
            print('конфет осталось ', numberofcandys)
            playercandys=int(input('введите число от 1 до 28 '))
            if playercandys > 28:
                print ('неверно, повторите ввод')
                playercandys=int(input('введите число от 1 до 28 '))
            numberofcandys-=playercandys
            print('конфет осталось ', numberofcandys)
    while numberofcandys>58:
            print ('ход компьютера')
            numberofcandys=numberofcandys-(numberofcandys-58)
            print('конфет осталось ', numberofcandys)
            playercandys=int(input('введите число от 1 до 28 '))
            if playercandys > 28:
                print ('неверно, повторите ввод')
                playercandys=int(input('введите число от 1 до 28 '))
            numberofcandys-=playercandys
    if numberofcandys==57:
            print ('ход компьютера')
            numberofcandys=numberofcandys-1
            print('конфет осталось ', numberofcandys)
            playercandys=int(input('введите число от 1 до 28 '))
            if playercandys > 28:
                print ('неверно, повторите ввод')
                playercandys=int(input('введите число от 1 до 28 '))
            numberofcandys-=playercandys
    while numberofcandys>29:
            print ('ход компьютера')
            numberofcandys=numberofcandys-(numberofcandys-29)
            print('конфет осталось ', numberofcandys)
            playercandys=int(input('введите число от 1 до 28 '))
            if playercandys > 28:
                print ('неверно, повторите ввод')
                playercandys=int(input('введите число от 1 до 28 '))
            numberofcandys-=playercandys
            print('конфет осталось ', numberofcandys)
    if numberofcandys==29:
        print ('ход компьютера')
        numberofcandys=numberofcandys-28
        print('конфет осталось', numberofcandys)
        playercandys=int(input('введите число от 1 до 28 '))
        if playercandys > 28:
            print ('неверно, повторите ввод')
            playercandys=int(input('введите число от 1 до 28 '))
        numberofcandys-=playercandys
        if numberofcandys<=0:
            print('игрок победил') 
    elif numberofcandys<29:
        print ('ход компьютера')
        print('осталось 0 конфет')
        print ('компьютер победил')
if generator == 2:
    print('всего конфет', numberofcandys)
    print('Первым ходит компьютер')
    while numberofcandys>86:
            print ('ход компьютера')
            numberofcandys=numberofcandys-28
            print('конфет осталось ', numberofcandys)
            playercandys=int(input('введите число от 1 до 28 '))
            if playercandys > 28:
                print ('неверно, повторите ввод')
                playercandys=int(input('введите число от 1 до 28 '))
            numberofcandys-=playercandys
            print('конфет осталось ', numberofcandys)
    while numberofcandys>58:
            print ('ход компьютера')
            numberofcandys=numberofcandys-(numberofcandys-58)
            print('конфет осталось ', numberofcandys)
            playercandys=int(input('введите число от 1 до 28 '))
            if playercandys > 28:
                print ('неверно, повторите ввод')
                playercandys=int(input('введите число от 1 до 28 '))
            numberofcandys-=playercandys
    if numberofcandys==57:
            print ('ход компьютера')
            numberofcandys=numberofcandys-1
            print('конфет осталось ', numberofcandys)
            playercandys=int(input('введите число от 1 до 28 '))
            if playercandys > 28:
                print ('неверно, повторите ввод')
                playercandys=int(input('введите число от 1 до 28 '))
            numberofcandys-=playercandys
    while numberofcandys>29:
            print ('ход компьютера')
            numberofcandys=numberofcandys-(numberofcandys-29)
            print('конфет осталось ', numberofcandys)
            playercandys=int(input('введите число от 1 до 28 '))
            if playercandys > 28:
                print ('неверно, повторите ввод')
                playercandys=int(input('введите число от 1 до 28 '))
            numberofcandys-=playercandys
            print('конфет осталось ', numberofcandys)
    if numberofcandys==29:
        print ('ход компьютера')
        numberofcandys=numberofcandys-28
        print('конфет осталось', numberofcandys)
        playercandys=int(input('введите число от 1 до 28 '))
        if playercandys > 28:
            print ('неверно, повторите ввод')
            playercandys=int(input('введите число от 1 до 28 '))
        numberofcandys-=playercandys
        if numberofcandys<=0:
            print('игрок победил') 
    elif numberofcandys<29:
        print ('ход компьютера')
        print('осталось 0 конфет')
        print ('компьютер победил')

rle=(input('введите текст '))
print(rle)
code = "" 
i = 0
while i < len(rle):
    count = 1
    while i + 1 < len(rle) and rle[i] == rle[i + 1]:
        count = count + 1
        i = i + 1
    code += str(count) + rle[i]
    i = i + 1
print(code)
