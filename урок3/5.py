def my_sum():
    sum_result = 0
    meaning = False
    while not meaning:
        number = input('Введите числа через пробел. Для завершения введите E: ').split()

        result = 0
        for el in range(len(number)):
            if number[el] == 'e' or number[el] == 'E':
                meaning = True
                break
            else:
                result = result + int(number[el])
        sum_result = sum_result + result
        print(f'Сумма введенный чисел равна {sum_result}')


my_sum()
