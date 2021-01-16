#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

a = [1, 2, 3]

def my_func(a, b, c):
    if a <= b and a <= c:
        return b + c
    elif b <= a and b <= c:
        return a + c
    else:
        return a+b


print(my_func(*a))