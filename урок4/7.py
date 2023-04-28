def my_gen(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
        yield x


my_num = int(input('Введите число: '))
for el in my_gen(my_num):
    print(el)
