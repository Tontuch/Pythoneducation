#6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
#Примеры строк файла:
#Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —

#Пример словаря:
#{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import re
with open('forquest5.txt', 'r') as open_obj:
    new_list = [el for el in open_obj.readlines()]
    print(new_list)
    new_dict = {}
    for el in new_list:
        el =el.split(': ', 1)
        print(el)
        el_list = [i for i in el[1].split(' ')]
        print(el_list)
        a = []
        for n in el_list:
            result = "".join(re.findall(r'\d+', n))
            print(result)
            if result != '':
                a.append(int(result))
        new_dict[el[0]] = sum(a)
print(new_dict)