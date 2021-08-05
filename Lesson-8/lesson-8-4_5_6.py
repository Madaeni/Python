# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class OwnException(Exception):
    def __init__(self, txt):
        self.txt = txt


class CompanyRoom:
    office_equipment = {
        "Принтер": [],
        "Сканнер": [],
        "Копир": []
    }
    office_equipment_all_room = {
        "Кабинет": [],
        "Бухгалтерия": [],
        "Склад": []
    }

    def add_equipment(self, name, equipment: list):
        for i in equipment:
            self.office_equipment[name].append(i)

    def add_equipment_all_room(self, room, equipment: dict):
        self.office_equipment_all_room[room].append(equipment)

    def validate_count(self):
        try:
            for value in self.office_equipment.values():
                if value[3].isdigit() is False:
                    raise OwnException("Количество должно быть числом!")
        except OwnException as err:
            print(err)


class Office(CompanyRoom):
    room = "Кабинет"
    office_equipment = {
        "Принтер": [],
        "Сканнер": [],
        "Копир": []
    }

    def count_office_equipment_office(self):
        my_list = []
        for value in self.office_equipment.values():
            my_list.append(int(value[3]))
        return sum(my_list)


class Accounting(CompanyRoom):
    room = "Бухгалтерия"
    office_equipment = {
        "Принтер": [],
        "Сканнер": [],
        "Копир": []
    }

    def count_office_equipment_accounting(self):
        my_list = []
        for value in self.office_equipment.values():
            my_list.append(int(value[3]))
        return sum(my_list)


class Warehouse(CompanyRoom):
    room = "Склад"
    office_equipment = {
        "Принтер": [],
        "Сканнер": [],
        "Копир": []
    }

    def count_office_equipment_warehouse(self):
        my_list = []
        for value in self.office_equipment.values():
            my_list.append(int(value[3]))
        return sum(my_list)


class OfficeEquipment:
    name: str
    serial: str

    @staticmethod
    def add_item(*args):
        return list(args)


class Printer(OfficeEquipment):
    name = "Принтер"
    serial: str
    is_color: bool


class Scanner(OfficeEquipment):
    name = "Сканнер"
    serial: str
    dpi: int


class Copier(OfficeEquipment):
    name = "Копир"
    serial: str
    is_laser: bool


my_warehouse = Warehouse()

my_warehouse.add_equipment(Printer().name, Printer().add_item("epson", False, "ep-12", "4"))
my_warehouse.add_equipment(Scanner().name, Scanner().add_item("hp", "123", "hp-12", "3"))
my_warehouse.add_equipment(Copier().name, Copier().add_item("xerox", True, "xe-12", "2"))

print(f"Список техники на складе {my_warehouse.office_equipment}")
my_result_warehouse = my_warehouse.count_office_equipment_warehouse()
print(f"Кол-во оргтехники на складе равно {my_result_warehouse}")

my_office = Office()
my_office.add_equipment(Printer().name, Printer().add_item("epson", True, "ep-34", "1"))
my_office.add_equipment(Scanner().name, Scanner().add_item("hp", "345", "hp-34", "1"))
my_office.add_equipment(Copier().name, Copier().add_item("xerox", True, "xe-34", "2"))

print(f"Список техники в кабинете: {my_office.office_equipment}")
my_result_office = my_office.count_office_equipment_office()
print(f"Кол-во оргтехники в кабинете равно {my_result_office}")

my_accounting = Accounting()
my_accounting.add_equipment(Printer().name, Printer().add_item("epson", True, "ep-56", "3"))
my_accounting.add_equipment(Scanner().name, Scanner().add_item("hp", "648", "hp-56", "2"))
my_accounting.add_equipment(Copier().name, Copier().add_item("xerox", False, "xe-56", "2"))

print(f"Список техники в бухгалтерии {my_accounting.office_equipment}")
my_result_acc = my_accounting.count_office_equipment_accounting()
print(f"Кол-во оргтехники в бухгалтерии равно {my_result_acc}")

my_company = CompanyRoom()
my_company.add_equipment_all_room(Office.room, my_warehouse.office_equipment)
my_company.add_equipment_all_room(Accounting.room, my_accounting.office_equipment)
my_company.add_equipment_all_room(Warehouse.room, my_accounting.office_equipment)

print(f"Общий список техниеи {CompanyRoom.office_equipment_all_room}")
my_result = my_result_warehouse + my_result_office + my_result_acc
print("Общее количество оргтехники равно", my_result)
