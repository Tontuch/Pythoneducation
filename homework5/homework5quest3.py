#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
import json

with open("forquest3.json", "r") as o_open:
    data = json.load(o_open)
    print(o_open)
    print(data)
    a = [el for el in data.values() if el < 20000]
    print(a)
    name =[name for name, salary in data.items() if salary < 20000]
    print(f"Оклад менее 20 тыс. руб. имеют сотрудники с фамилиями {name}")

