#задача 1
day = int(input('введите день недели '))
if 5<day:
    print('день выходной')
elif day>8:
    print('такого дня нет')
else:
    print('день рабочий')
#задача 2

lx = int(input('число X '))
ly = int(input('число Y '))
lz = int(input('число X '))
first = not (lx or ly or lz)
second = not lx and not ly and not lz
if first == second:
    print('утверждение истинно')
else:
    print('утверждение ложно')

#задача 3
x =int(input('введите x '))
y =int(input('введите y '))
if (x>0) & (y>0):
    print('первая четверть')
elif (x<0) & (y>0):
    print('вторая четверть')
elif (x<0) & (y<0):
    print('третья четверть')
else:
    print('четвертая четверть')
#задача 4
quarter = int(input('введите четверть '))
if quarter == 1:
    print('x>0 y>0')
elif quarter == 2:
    print('x<0 y>0')
elif quarter == 3:
    print('x<0 y<0')
elif quarter == 4:
    print('x>0 y<0')
else:
    print("такой четверти нет")

#задача 5
ax = int(input('введите координату X точки А '))
ay = int(input('введите координату Y точки А '))
bx = int(input('введите координату X точки B '))
by = int(input('введите координату Y точки B '))
result = ((bx-ax)*(bx-ax)+(by-ay)*(by-ay))**0.5
print(result)

