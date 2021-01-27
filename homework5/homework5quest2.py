#2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("forquest2.txt") as p_open:
    a = p_open.readlines()
    print(a)
    b = len(a)
    print(f"количество строк в файле {b}")
    n = 0
    while n < b:
        word = [el for el in a[n].split(" ")]
        cnt_word = len(word)
        print(f"количество слов в {n + 1} строке равно {cnt_word}")
        n += 1






