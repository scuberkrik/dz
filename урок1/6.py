revenue = float(input('Введите выручку: '))
costs = float(input('Введите издержки: '))
if revenue > costs:
    print('прибыль — выручка больше издержек')
    print(f'Рентабельность выручки :{revenue / costs:.2f}')
    staff = int(input('Введите число сотрудников: '))
    print(f'Прибыль в расчете на одного сторудника: {revenue / staff:.2f}')
elif revenue == costs:
    print('Выручка равна издержкам')
else:
    print('убыток — издержки больше выручки')
