from math import fabs
import random


#Частина перша
print('Частина перша\n')

x = 'Максим'
y = 'Кунда'

print("Ім'я:",x)
print("Прізвище:",y)

z = x + ' ' + y

print("Результат об'єднання:",z)

n = 1

print('Результат розрахунку:',(n + fabs(n%5))*(n%10))

#Частина друга
print('\nЧастина друга\n')

str = ""

for i in range(10 + n%5):
    str += 'A'

print("Рядок довжиною (10 + N mod 5) =", 10 + n%5, ":" , str)

#x_arr2 = [0] * 60 + [random.randint(1, 100) for _ in range(40)]
#random.shuffle(x_arr)

x_arr = [0, 0, 1, 2, 45, 0, 24,354, 43523, 12, 0 ,0, 0, 0, 24,253,35, 0]

print('Масив',x_arr)

index = 0
index_first = -1
index_last = -1
len = 0
max_len = 0
end_index_first = -1
end_index_last = -1
target = False

for i in x_arr:
    if i == 0:
        if target == False:
            target = True
            len = 1
            index_first = index
        else:
            len += 1
    else:
        target = False
        index_last = index
        if max_len < len:
            max_len = len
            end_index_first = index_first
            end_index_last = index_last

    index += 1

print('Довжина серії:',max_len, '\nІндекс першого елементу серії:' ,end_index_first, '\nІндекс останього елементу серії:' ,end_index_last)


