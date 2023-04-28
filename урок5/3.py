with open('file3.txt', 'r', encoding='UTF-8') as file:
    average_salary = 0
    lines = file.readlines()
    print(f'Сотрудники у которых зп меньше 20000')
    for line in lines:
        worker, salary = line.split()
        salary = float(salary)
        average_salary += salary
        if salary < 20000:
            print(f'{worker} {salary}')
    if len(lines) > 0:
        average_salary /= len(lines)
        print(f"Средняя зарплата: {average_salary:.2f}")
