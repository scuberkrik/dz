class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def full_name(self):
        return f"{self.name} {self.surname}"

    def total_income(self):
        return sum(self._income.values())


x = Position(input('Введите имя: '),
             input('Введите фамилию: '),
             input('Введите должность: '),
             int(input('Введите оклад: ')),
             int(input('Введите премию: '))
             )
print(f'Имя---------{x.full_name()}\n'
      f'Должность---{x.position}\n'
      f'Доход-------{x.total_income()}'
      )
