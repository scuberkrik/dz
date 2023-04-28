class Warehouse:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"Товар {item} не найден на складе")

    def transfer_item(self, item, department):
        if item in self.items:
            self.items.remove(item)
            department.receive_item(item)

    def display_items(self):
        print("Товары на складе:")
        for item in self.items:
            print(item)


class OfficeEquipment:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        try:
            self.price = float(price)
        except ValueError:
            print("Недопустимое значение цены.")

    def __str__(self):
        return f"{self.__class__.__name__} - {self.brand} {self.model} - ${self.price}"


class Printer(OfficeEquipment):
    def __init__(self, brand, model, price, printable_colors: bool):
        super().__init__(brand, model, price)
        if isinstance(printable_colors, bool):
            self.printable_colors = printable_colors
            if printable_colors:
                print("Цветой")
            elif not printable_colors:
                print("Черно-белый")
        else:
            print("Недопустимое значение для is_color. Должно быть True или False.")


class Scanner(OfficeEquipment):
    def __init__(self, brand, model, price, scanning_resolution):
        super().__init__(brand, model, price)
        try:
            self.scanning_resolution = int(scanning_resolution)
        except ValueError:
            print("Недопустимое значение разрешения.")


class Photocopier(OfficeEquipment):
    def __init__(self, brand, model, price, speed):
        super().__init__(brand, model, price)
        try:
            self.speed = float(speed)
        except bool:
            print("Недопустимое значение скорости.")


class Department:
    def __init__(self, name):
        self.name = name
        self.items = []

    def receive_item(self, item):
        self.items.append(item)

    def display_items(self):
        print(f"Элементы в {self.name} отделе:")
        for item in self.items:
            print(item)


warehouse = Warehouse()
printer = Printer("HP", "LaserJet Pro M15w", 200, False)
scanner = Scanner("Canon", "CanoScan LiDE 400", 90, "4800 dpi")
photocopier = Photocopier("Xerox", "B1025", 1200, 25)

warehouse.add_item(printer)
warehouse.add_item(scanner)
warehouse.add_item(photocopier)
warehouse.display_items()

it_department = Department("IT")
hr_department = Department("БУХ")

warehouse.transfer_item(printer, it_department)
warehouse.transfer_item(scanner, hr_department)

it_department.display_items()
hr_department.display_items()
