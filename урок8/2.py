class DZE(Exception):
    pass


try:
    num = int(input("Введите числитель: "))
    den = int(input("Введите знаменатель: "))
    if den == 0:
        raise DZE("Деление на ноль запрещено!")
    result = num / den
    print(f"Результат деления: {result}")
except ValueError:
    print("Ошибка ввода числа!")
except DZE as e:
    print(e)
except Exception as e:
    print(f"Произошла ошибка: {e}")
