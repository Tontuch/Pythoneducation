#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_stroke = input("Введите сторку")
print(user_stroke)
a = [str(i) for i in user_stroke.split(" ")]
print(a)
n = 1
for el in a:
    if len(el) < 10:
        print(f"{n}){el}")
        n = n+1
    else:
        print(f"{n}){el[0:10]}")
        n = n+1