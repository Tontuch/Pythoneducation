#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random
from functools import reduce
new_list = []
def summ(a, b):
    return a + b
n = 0
while n <= 10:
    a = random.randint(0, 10)
    new_list.append(a)
    n += 1
print(new_list)
new_line = ' '.join(str(el) for el in new_list)
print(new_line)
with open('forquest5.text', 'w') as open_obj:
    open_obj.writelines(new_line)
with open('forquest5.text', 'r') as open_obj:
    a = [int(el) for el in open_obj.readline().split(" ")]
    print(reduce(summ, a))