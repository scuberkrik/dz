my_num = int(input('Введите число: '))
max_digit = 0
while my_num > 0:           #Цикл начиная с последней цифры введённого числа "х" ищет самую большую цифру "max_digit"
    x = my_num % 10
    if x > max_digit:
        max_digit = x
    my_num = my_num//10

print(f'Самая большая цифра в числе:{max_digit}')




