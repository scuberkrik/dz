my_list = ['Зима', 'Весна', 'Лето', 'Осень']
x = int(input('Введите номер месяца: '))
if 12 >= x >= 1:
    if 3 <= x <= 5:
        print(my_list[1])
    elif 6 <= x <= 8:
        print(my_list[2])
    elif 9 <= x <= 11:
        print(my_list[3])
    else:
        print(my_list[0])
else:
    print(f'Месяца под номером {x} не существует! Введите корректное значение от 1 до 12!')


