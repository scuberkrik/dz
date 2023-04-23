from itertools import count, cycle

print('Первый скрипт.')
for i in count(3):
    if i > 10:
        break
    else:
        print(i)

print('Скрипт 2.')
x = 0
my_list = [1, 2, 3, 4, 5]
for el in cycle(my_list):
    if x >= 10:
        break
    else:
        x += 1
        print(el)
