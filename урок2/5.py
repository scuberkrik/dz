rating = [7, 5, 3, 3, 2]
new_rating = int(input('Добавьте значение рейтинга: '))
if new_rating > 0:
    rating.append(new_rating)
    rating.sort(reverse=True)
    print(rating)
else:
    print('Введите натуральное число')
