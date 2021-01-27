#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
translate = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('forquest4.txt', 'r') as o_open:
    for el in o_open:
        el = el.split(' ', 1)
        print(el)
        new_file.append(f'{translate.get(el[0])}{el[1]}')
print(new_file)
with open('forquest4transl.txt', 'w') as wr_data:
    wr_data.writelines(new_file)




