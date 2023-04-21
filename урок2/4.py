my_string = input('Введите несколько слов через пробел: ').split()
my_num = 0
for i in range(0, len(my_string), 1):
    my_num += 1
    print(f'{my_num}:{my_string[i][0:10]}')
