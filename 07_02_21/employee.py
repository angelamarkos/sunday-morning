import csv
import os
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, id, name, title, level):
        self.id = id
        self.name = name
        self.title = title
        self.level = level

    @abstractmethod
    def calculate_pay(self):
        pass

    def __str__(self):
        return f'{self.name} - {self.title}'

class Bonus(ABC):
    def __init__(self, commision_sales, percent):
        self.bonus = int(commision_sales) * int(percent) / 100

class SalaryEmployee(Employee):
    def __init__(self, id, name, title, level, salary):
        super().__init__(id, name, title, level)
        self.salary = int(salary)

    def calculate_pay(self):
        return self.salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, title, level, salary, hours_worked):
        super().__init__(id, name, title, level)
        self.salary = int(salary)
        self.hours_worked = int(hours_worked)

    def calculate_pay(self):
        return self.salary * self.hours_worked

class BonusSalaryEmployee(SalaryEmployee, Bonus):
    def __init__(self, id, name, title, level, salary, commision_sales, percent):
        SalaryEmployee.__init__(self, id, name, title, level, salary)
        Bonus.__init__(self, commision_sales, percent)

    def calculate_pay(self):
        return self.salary + self.bonus


class BonusHourlyEmployee(HourlyEmployee, Bonus):
    def __init__(self, id, name, title, level, salary, hours_worked, commision_sales, percent):
        super().__init__(id, name, title, level, salary, hours_worked)
        Bonus.__init__(self, commision_sales, percent)

    def calculate_pay(self):
        return self.salary * self.hours_worked + self.bonus

class Manager(SalaryEmployee):
    def __init__(self, id, name, title, level, salary):
        super().__init__(id, name, title, level, salary)

    def calculate_pay(self):
        return 1.1 * self.salary

class FactoryEmployee:
    CLASS_MAPPING = {
        "salary": SalaryEmployee,
        "hourly": HourlyEmployee,
        "bonus_hourly": BonusHourlyEmployee,
        "bonus_salary": BonusSalaryEmployee,
        "manager": Manager
    }

    @staticmethod
    def get_employee_type(line):
        if line.get('hourly') == 'Yes':
            employee_type = 'hourly'
        else:
            employee_type = 'salary'
        if line.get('commision_sales'):
            employee_type = f'bonus_{employee_type}'
        return employee_type

    @staticmethod
    def get_employee(employee_type, *args, **kwargs):
        EmployeeClass = FactoryEmployee.CLASS_MAPPING[employee_type]
        kwargs = {k: v for k, v in kwargs.items() if k in EmployeeClass.__init__.__code__.co_varnames}
        return EmployeeClass(*args, **kwargs)

    @classmethod
    def get_employees(cls, csv_path):
        with open(csv_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for line in reader:
                yield cls.get_employee(cls.get_employee_type(line), **line)


csv_path = os.path.normpath('./employee_data.csv')
for employee in FactoryEmployee.get_employees(csv_path):
    print(employee, employee.calculate_pay())


# employee_1 = FactoryEmployee.get_employee("salary", 1, "Jim Jackson", "Sofware Engineer", "inter", 1000)
# employee_5 = FactoryEmployee.get_employee("manager", 5, "Jim Jackson", "Sofware Engineer", "inter", 1000)
# employee_2 = FactoryEmployee.get_employee("hourly", 2, "John Jackson", "Sofware Engineer", "senior", 80, 25)
# employee_3 = FactoryEmployee.get_employee("bonus_salary", 3, "John Robertson", "Sales manager", "senior", 6000 ,80000, 8)
# employee_4 = FactoryEmployee.get_employee("bonus_hourly", 4, "Jack Roberson", "Sales manager", "mid", 4000, 30, 50000, 3)
#
# print(employee_1, employee_1.calculate_pay())
# print(employee_2, employee_2.calculate_pay())
# print(employee_3, employee_3.calculate_pay())
# print(employee_4, employee_4.calculate_pay())







