#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

#Подсказка: использовать менеджеры контекста.
import json
firm_profit = {}
firm_loss = {}
firm_zero = {}

#average ={'average_profit', a}
with open('forquest7.txt', 'r') as open_obj:
    new_list = open_obj.readlines()
    for el in new_list:
        el = el.split(' ')
        profit = int(el[2]) - int(el[3])
        if profit > 0:
            firm_profit[f'{el[1]}{el[0]}'] = profit
        elif profit < 0:
            firm_loss[f'{el[1]}{el[0]}']= profit
        else:firm_zero[f'{el[1]}{el[0]}']= profit
avg = {'average_profit':sum(firm_profit.values())/len(firm_profit.values())}

result_list =[firm_profit, avg, firm_zero, firm_loss]

print(result_list)
with open('forquest7.json', 'w') as my_jsonobj:
    json.dump(result_list, my_jsonobj)