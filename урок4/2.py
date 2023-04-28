result = []
my_list = [int(el) for el in input("Введите список чисел: ").split()]
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        (result.append(my_list[i]))
print(f'Исходный список {my_list} \n'
      f'Результат {result}')

