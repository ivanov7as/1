length = int(input('введите длину списка '))
new_list = []
sum = 0
for _ in range(length):
    num=int(input())
    new_list.append(num)
for i in range(1, length):
    if i %2>0:
        sum+= new_list[i]
print(sum)

number = int(input('введите длину списка '))
first_list = []
second_list=[]
sum = 0
for _ in range(number):
    n=int(input())
    first_list.append(n)
for i in range((number-1)//2+1):
    m=first_list[i] * first_list[number-i-1]
    second_list.append(m)
print(second_list)

import math
number_float = int(input('введите длину списка '))
list_float = []
for _ in range(number_float):
    n=float(input())
    if n > 0:
        n=n-math.trunc(n)
    list_float.append(n)
print(list_float)
minn=float(list_float[0])
maxx=float(list_float[0])
for i in range(0, number_float):
    if list_float[i]<minn:
        minn=list_float[i]
    elif list_float[i]>maxx:
        maxx=list_float[i]
print(maxx-minn)


digit_d = int(input('введите число '))
digit_b=''
while digit_d>0:
    digit_b=digit_b+str(digit_d%2)
    digit_d=digit_d//2
print(digit_b)

f = int(input("введите число Фирбоначчи "))
fp1 = fp2 = 1
fibn=[]
fibp=[]
fibf=[]
fn1=1
fn2=-1
for i in range(-f, -2):
    fib_n = fn1 - fn2
    fn1 = fn2
    fn2 = fib_n
    fibn.append(fn2)
fibn.reverse()
fibn.append(-1)
fibn.append(1)
fibn.append(0)
fibn.append(1)
fibn.append(1)
for i in range(2, f):
    fib_p = fp1 + fp2
    fp1 = fp2
    fp2 = fib_p
    fibp.append(fp2)
fibf=fibn+fibp
print(fibf)
