

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
digitString='000000000'

i=1
while i<6:
    print(i,digitString)
    i=i+1
else:
    print('Count is over')
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
count=0

for i in range(10):
   digit=input("введите число: \t")
   digit=int(digit)
   if digit==5: count+=1
if count==0: print('В цифрах нет 5')
print('Коллическтво пятерок равно ', count)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0

for i in range(1,101):
    sum+=i
print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
mult=1

for i in range(1,11):
    mult*=i
print(mult)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

digit=2129
digit=str(digit)[::-1]
digit=int(digit)

while digit>0:
    print(digit%10)
    digit =digit//10

'''
Задача 6
Найти сумму цифр числа.
'''
sum=0
digit=input('Введите число')
digit=int(digit)
while digit>0:
     sum=(digit%10)+sum
     digit=digit//10
print(sum)



'''
Задача 7
Найти произведение цифр числа.
'''
mult=1
digit=input('Введите число')
digit=int(digit)
while digit>0:
     mult=(digit%10)*mult
     digit=digit//10
print(mult)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 213413
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
count=0
max=0
digit=int(input('введите число '))

while digit>0:
    count=(digit%10)
    if count>max:max=count
    digit=digit//10
print(max)

'''
Задача 10
Найти количество цифр 5 в числе
'''
count=0
digit=int(input('введите число '))

while digit>0:
    if digit%10==5:count+=1
    digit=digit//10

if count==0:print("нет пятерок")
else:print(count)