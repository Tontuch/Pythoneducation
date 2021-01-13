#4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

x = 4
y = -3

def involution (x,y):
    return x**y

print(involution(x,y))

def involution_2 (x,y):
    i = abs(y)
    result = 1
    while i != 0:
        result = result / x
        i = i - 1
    return result
print(involution_2(x, y))
