class Stationery:
    title = "Канцелярская принадлежность"

    def draw(self):
        print('запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')


class Pencil(Stationery):
    def draw(self):
        print("Отрисовка карандашом")


class Handle(Stationery):
    def draw(self):
        print("Отрисовка маркером")


print(Stationery().title)
Stationery().draw()

p = Pen()
p.draw()

penc = Pencil()
penc.draw()

h = Handle()
h.draw()
