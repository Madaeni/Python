# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень).

# Решения через list:

month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
month_list = ["Зима", "Весна", "Лето", "Осень"]

if month < 3 or month == 12:
    print(month_list[0])
elif 3 <= month <= 5:
    print(month_list[1])
elif 6 <= month <= 8:
    print(month_list[2])
else:
    print(month_list[3])

# Решения через dict:

month_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето",
              7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}

print(month_dict[month])