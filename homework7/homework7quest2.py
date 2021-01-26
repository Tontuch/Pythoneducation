#2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
# и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property

class Clothes:
    def __init__(self, name):
        self.name = name


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
    @property
    def consumption_coat(self):
        return self.size/6.5 + 0.5

class Suit(Clothes):
    def __init__(self, name, hight):
        super().__init__(name)
        self.hight = hight
    @property
    def consuption_suit(self):
        return (self.hight * 2) + 0.3


coat1 = Coat('Пальто', 52)
suit1 = Suit('Пиджак', 52)
union_consamption = coat1.consumption_coat + suit1.consuption_suit
print(coat1.consumption_coat)
print(suit1.consuption_suit)
print(union_consamption)

