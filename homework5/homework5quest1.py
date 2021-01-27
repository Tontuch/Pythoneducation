#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


open_o = open("mytextfile.txt", 'w')

#a = [el + "\n" for el in input("Введите данные").split(" ")]
#with open_o:
    #open_o.writelines(a)
a = []

while True:
    i = (input("Введите данные"))
    if i == "":
        print(a)
        break
    else:
        n = (i + "\n")
        a.append(n)

with open_o:
    open_o.writelines(a)
open_o = open("mytextfile.txt", 'r')
with open_o:
    my_text = open_o.readlines()
    print(*my_text)


