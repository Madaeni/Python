# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.


def to_int(s):
    try:
        return int(s)
    except:
        return s


my_list = []
sum_list = []
n = 0

with open("lesson-5-3.txt", "r") as salary:
    while True:
        my_str = salary.readline()
        if not my_str:
            break
        else:
            my_str = my_str.split()
            my_str = [to_int(n) for n in my_str]
            sum_list.append(my_str[1])
            if my_str[1] < 20000:
                my_list.append(my_str[0])
        n += 1

print(f"Оклад менее 20000 у сотрудников: {', '.join(my_list)}")
print(f"Средняя величина дохода сотрудников равна: {sum(sum_list) // n}")



