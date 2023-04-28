class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name}  поехала'

    def stop(self):
        return f'{self.name}  остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'скорость {self.name} равна {self.speed}'

    def police(self):
        if self.is_police:
            return f'{self.name} это полицейская машина'
        else:
            return f'{self.name} это не полицейская машина'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'скорость {self.name} равна {self.speed}, превышение скорости на {self.speed - 60}'
        else:
            return f'скорость {self.name} равна {self.speed}, скорость не превышена'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'скорость {self.name} равна {self.speed}, превышение скорости на {self.speed - 40} '
        else:
            return f'скорость {self.name} равна {self.speed}, скорость не превышена'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


bmw = SportCar(100, 'Красный', 'Bmw', False)
oka = TownCar(80, 'Белый', 'Oka', False)
lada = WorkCar(40, 'Черный', 'Lada', False)
uaz = PoliceCar(90, 'Синий', 'Uaz', True)

print(f'{bmw.go()}. {bmw.show_speed()}. {bmw.police()}')
print(f'{oka.go()}.{oka.show_speed()}. {oka.police()}')
print(f'{lada.show_speed()}. {lada.turn_left()}. Цвет {lada.name} {lada.color}')
print(f'{uaz.stop()}. Цвет {uaz.name} {uaz.color}. {uaz.police()}')
