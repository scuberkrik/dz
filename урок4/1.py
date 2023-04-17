def my_func(hours, salary, bonus):
    return hours * salary + bonus


print('Расчет зарплаты сотрудника по выработке в часах.')
print(my_func(int(input('Введите часы: ')),
              int(input('Введите стоимость часа: ')),
              int(input('Введите премию: '))
              ))
