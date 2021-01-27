#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться
# после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#ользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
answer = int(input("Введите число рейтинга"))

if (answer in my_list) is False:
    n = 0
    while (answer in my_list) is False:
        if answer > my_list[n]:
            my_list.insert(n, answer)
        elif answer < my_list[n] and answer > my_list[len(my_list)-1]:
            n = n + 1
        else:
            my_list.append(answer)
else:
    a = my_list.index(answer)
    b = my_list.count(answer)
    my_list.insert((a+b), answer)

print(my_list)