# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


a = [int(i) for i in input("Введите 2 числа через пробел").split(" ")]
#print(a)
#a = float(input("Введите первое число"))
#b = float(input("Введите второе чило"))
def division (a,b):
    if b != 0:
        return a / b
    else:
      return "На ноль делить нельзя!"

print(division(*a))
