def my_info(name, lastname, year_of_birth, city, email, phone):
    return print(f"Имя: {name} Фамилия: {lastname} Год: {year_of_birth} Город: {city} Почта: {email} Телефон: {phone}")


my_info(name=input('Введите имя: '), lastname=input('Введите фамилию: '), year_of_birth=input('Введите год Рождения: '),
        city=input('Введите город проживания: '), email=input('Введите ваш email: '), phone=input('Введите телефон: '))
