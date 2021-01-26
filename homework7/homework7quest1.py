#Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
#Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

#31 22
#37 43
#1 86

#3 5 32
#2 4 6
#-1 64 -8

#3 5 8 3
#8 3 7 1
#Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (
# двух матриц). Результатом сложения должна быть новая матрица.
#одсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix1):
        self.matrix1 = matrix1



    def __str__(self):
        trans_matrix1 = '\n'.join(['\t'.join([str(el) for el in i]) for i in self.matrix1])
        return f'Матрица\n{trans_matrix1}'

    def __add__(self, other):
        empty_matrix = []
        for i in range(len(self.matrix1)):
            empty_matrix.append([0] * len(self.matrix1[i]))
        for el in range(len(self.matrix1)):
            for i in range(len(self.matrix1[el])):
                empty_matrix[el][i] = self.matrix1[el][i] + other.matrix1[el][i]
        return empty_matrix


matrix_1 = [[31, 22], [37, 43], [1, 86]]

matrix_2 = [[10, 34], [23, 16], [6, 7]]

matrix_3 = [[5, 7], [10, 15], [65, 32]]

m1 = Matrix(matrix_1)
m2 = Matrix(matrix_2)
m3 = Matrix(matrix_3)
print(m3)
print(m1 + m3)