# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

user_profile = {'name': "Анатолий", 'surname': "Шорохов", 'city': "Хабаровск", 'email': "vombat2006@mail.ru",
                'fon_namber': "89142129369"}


def one_strngh(name, surname, city, email, fon_namber):
    return (f"{surname} {name} город проживания {city} эллектронный адрес {email} номер телефона {fon_namber}")

print(one_strngh(**user_profile))
