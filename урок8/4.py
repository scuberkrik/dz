class Warehouse:
    def __init__(self):
        self.storage = {}


class OfficeEquipment:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, brand, model, price, printable_colors):
        super().__init__(brand, model, price)
        self. printable_colors = printable_colors


class Scanner(OfficeEquipment):
    def __init__(self, name, model, price, scanning_resolution):
        super().__init__(name, model, price)
        self.scanning_resolution = scanning_resolution


class Photocopier(OfficeEquipment):
    def __init__(self, name, model, price, speed):
        super().__init__(name, model, price)
        self.speed = speed


printer = Printer("HP", "LaserJet Pro", 200, "Черно-белый")
scanner = Scanner("Canon", "ScanMaster", 100, "4800 dpi")
photocopier = Photocopier("Xerox", "Ultimate", 250, 25)

print(printer .brand, printer.model, printer.price, printer.printable_colors)
print(scanner.brand, scanner.model, scanner.price, scanner.scanning_resolution)
print(photocopier.brand, photocopier.model, photocopier.price, photocopier.speed)
