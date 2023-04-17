def my_division():
    try:
        arg1 = int(input('Введите делимое: '))
        arg2 = int(input('Введите делитель: '))
    except ZeroDivisionError:
        return 'Делитель не может быть равен нулю!'
    except ValueError:
        return 'Вы ввели не число!'
    return arg1 / arg2


print(my_division())
