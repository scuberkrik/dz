my_list = []
n = 1
while True:
    print('Введите данные')
    title = input('Название товара: ')
    if title == '':
        break
    price = int(input('цена товара: '))
    quantity = int(input('кол-во товара: '))
    uom = input('единица измерения: ')
    my_list.append((n, {'Название': title, 'Цена': price, 'Количество': quantity, 'Единица измерения': uom}))
    n += 1
    print('Для завершения ввода данных оставте поле "название товара" пустым!')
rep_title = []
rep_price = []
rep_quan = []
rep_uom = []
for i in my_list:
    rep_title.append(i[1].get('Название'))
    rep_price.append(i[1].get('Цена'))
    rep_quan.append(i[1].get('Количество'))
    rep_uom.append(i[1].get('Единица измерения'))
print(f'Отчет \n'
      f'---------------------------------------------------------------------------------------------------- \n'
      f'Название:    {rep_title} \n'
      f'Цена:        {rep_price} \n'
      f'Количество:  {rep_quan} \n'
      f'Ед:          {rep_uom}')
