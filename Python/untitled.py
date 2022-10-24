number = float(input('введите число '))
d = float(input('введите точность '))
s = str(d)
numoverdot = (abs(s.find('.') - len(s)) - 1)
print(round(number, numoverdot))

n=int(input('введите число N '))
for i in range(2, n//2 + 1):
    if (n % i == 0):
        print(i)
        n //= i

first = [1, 2 ,2 ,3 ,4, 4, 4 ,5, 5 ,6 ,7 ,8, 8, 8]
second = []
for i in range(1, len(first)):
    if first.count(i)==1:
        second.append(i)
print(second)

from random import randint
k = int(input('введите  степень k '))
num=[randint(0,100) for i in range(k)]+[randint(1,100)]
eq=' + '.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(num) if j][::-1])
eq=eq.replace('x^1', 'x')
eq=eq.replace('x^0', '')
eq=eq+' = 0'
print(eq)
with open('file.txt', 'w') as file:
    file.write(eq)
