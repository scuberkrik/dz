dayz = int(input('Введите результат первого дня в км: '))
result = int(input('Введите желаемый результат: '))
day_num = 1
while dayz < result:
    dayz = dayz+dayz*0.1
    day_num = day_num+1

print(f'Спортсмен достигнет желаемого результата на {day_num} день')

