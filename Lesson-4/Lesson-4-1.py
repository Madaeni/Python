# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary(hour, per_hour, bonus):
    try:
        result = int(hour) * int(per_hour) + int(bonus)
        print(f"Заработная плата составляет {result}")
    except ValueError:
        print("Все параметры должны быть числами")

    return


script_name, first_param, second_param, third_param = argv

print("Засчет заработной платы:", script_name)
print("Выработка в часах:", first_param)
print("Ставка в час:", second_param)
print("Премия:", third_param)

salary(hour=first_param, per_hour=second_param, bonus=third_param)