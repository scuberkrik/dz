my_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
x = int(input('Введите номер месяца: '))
if 12 >= x >= 1:
    if 3 <= x <= 5:
        print(my_dict.get(2))
    elif 6 <= x <= 8:
        print(my_dict.get(3))
    elif 9 <= x <= 11:
        print(my_dict.get(4))
    else:
        print(my_dict.get(1))
else:
    print(f'Месяца под номером {x} не существует! Введите корректное значение от 1 до 12!')

