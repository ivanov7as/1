number = int(input('введите число '))
sum = 0 
while number > 0:
    sum = sum + number % 10
    number = number // 10
print("Сумма цифр:", sum)

n = int(input('введите число N '))
count =1 
for i in range(1, n+1):
    count = count*i
    print(count, end=' ')

num = int(input('введите число N '))
c=0
for i in range(1, num+1):
    c=c+(1+1/i)**i
print(c)

from random import randint
nlist=int(input('введите число '))
list=[]
for i in range(nlist):
    list.append(randint(-nlist, nlist))
file=1
with open('file.txt', 'w') as txt:
    for i in range(nlist):
        txt.write(str(randint(0, nlist-1))+ '\n')
with open('file.txt', 'r') as txt:
    txt=txt.read().splitlines()
    for number in txt:
        file*=list[int(number)]
print(file)
