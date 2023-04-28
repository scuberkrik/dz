def my_func(a, b, c):
    return print(f'Сумма двух наибольших чисел равна {a + b + c - min([a, b, c])}')


my_func(
    int(input('Введите первое число: ')),
    int(input('Введите второе число: ')),
    int(input('Введите третье число: ')),
)
