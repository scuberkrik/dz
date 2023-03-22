my_time = int(input('Введите время в секундах: '))
hours = my_time//3600
minutes = (my_time % 3600)//60
seconds = (my_time % 3600) % 60
if hours > 24:                                               #Условие если введенное время превышает 24 часа в сутках
    print('Введенное время превышает 24 часа в сутках')
else:
    print(f'Время: {hours}:{minutes}:{seconds}')


