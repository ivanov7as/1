list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(list):
    if list[i].isdigit():
        list.insert(i, '"')
        list.insert(i + 2, '"')
        i+=1
    i += 1
j=0
while j<len(list):
    if list[j].isdigit():
        list[j] = list[j].zfill(2)
        j+=1
    j+=1
k=0
while k<len(list):
    if '+' in list[k]:
        list[k] = list[k][1:].zfill(2)
        list[k] = "+" + list[k].replace(" ", "+")
        list.insert(k, '"')
        list.insert(k + 2, '"')
        k+=1
    k+=1
print(list)

arr = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for name in arr:
    print('Привет,', name.split()[-1].title(),'!')

price = [57.8, 46.51, 97, 22.3, 32, 41.3, 55, 88, 77.22, 31]
price=["%.2f" % i for i in price]
for num in price:
    print(num.split('.')[0].title(), 'рублей', num.split('.')[-1].title(),'копеек')
