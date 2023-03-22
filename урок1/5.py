revenue = float(input('Введите выручку: '))
costs = float(input('Введите издержки: '))
if revenue > costs:
    print('прибыль — выручка больше издержек')
elif revenue == costs:
    print('Выручка равна издержкам')
else:
    print('убыток — издержки больше выручки')
