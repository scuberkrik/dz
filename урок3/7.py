def int_func(a):
    return a.title()


my_list = []
for i in input('Введите слова в нижнем регистре через пробел: ').split():
    my_list.append(int_func(i))

print(" ".join(my_list))
