# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

def form(name, family, birthday, city, email, phone):
    your_form = [name, family, birthday, city, email, phone]
    return print(your_form)


your_name = input("Введите имя: ")
your_family = input("Введите фамилию: ")
your_birthday = int(input("Введите год рождения: "))
your_city = input("Введите город проживания: ")
your_email = input("Введите email: ")
your_phone = input("Введите телефон: ")

form(
    name=your_name,
    family=your_family,
    birthday=your_birthday,
    city=your_city,
    email=your_email,
    phone=your_phone
)


