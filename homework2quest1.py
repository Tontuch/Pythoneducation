#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = (1, False, "Привет", 0, 10.5, -8, True)
print(my_list, len(my_list))
for n in my_list:
    print(type(n))