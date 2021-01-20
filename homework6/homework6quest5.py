#5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw (self):
        return 'Запуск отрисовки'
class Pen(Stationery):
    def draw(self):
        return 'Рисуем ручкой'
class Pencil(Stationery):
    def draw(self):
        return 'Рисуем карандашом'
class Handle(Stationery):
    def draw(self):
        return 'Рисуем маркером'

stationery_1 = Stationery('Рисование')
print(stationery_1.draw())
stationery_2 = Pen('Ручка')
print(stationery_2.draw())
stationery_3 = Pencil('Карандаш')
print(stationery_3.draw())
stationery_4 = Handle('Маркер')
print(stationery_4.draw())


