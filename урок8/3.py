class NotNumberError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Ошибка! {self.value} не является числом.'


number_list = []
while True:
    try:
        user_input = input('Введите число, для завершения введите "stop": ')
        if user_input == 'stop':
            break
        if not user_input.isnumeric():
            raise NotNumberError(user_input)
        number_list.append(int(user_input))
    except NotNumberError as e:
        print(e)

print(f'Список чисел: {number_list}')
