# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, Вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

a = int(input("Выручка: "))
b = int(input("Издержки: "))
if a > b:
    print("Прибыль")
    c = (a - b) / b * 100
    print(f"Ваша рентабельность {c}%")
elif a == b:
    print("Вышли в ноль")
else:
    print("Убыток")
if a > b:
    d = int(input("Количество работников: "))
    f = (a - b) / d
    print(f"Ваша прибыль на каждого сотрудника состовляет {f}")