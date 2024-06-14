from typing import List

class Employee:
    def __init__(self, name: str, salary: float):
        self.__name = name
        self.__salary = salary
        self.__bonus = 0.0

    @property
    def name(self) -> str:
        return self.__name

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, value: float):
        self.__salary = value

    def set_bonus(self, bonus: float):
        self.__bonus = bonus

    def to_pay(self) -> float:
        return self.__salary + self.__bonus


class SalesPerson(Employee):
    def __init__(self, name: str, salary: float, percent: float):
        super().__init__(name, salary)
        self.__percent = percent

    def set_bonus(self, bonus: float):
        if self.__percent > 200:
            bonus *= 3
        elif self.__percent > 100:
            bonus *= 2
        super().set_bonus(bonus)


class Manager(Employee):
    def __init__(self, name: str, salary: float, client_amount: int):
        super().__init__(name, salary)
        self.__client_amount = client_amount

    def set_bonus(self, bonus: float):
        if self.__client_amount > 150:
            bonus += 1000
        elif self.__client_amount > 100:
            bonus += 500
        super().set_bonus(bonus)


class Company:
    def __init__(self, employees: List[Employee]):
        self.employees = employees

    def give_everybody_bonus(self, company_bonus: float):
        for employee in self.employees:
            employee.set_bonus(company_bonus)

    def total_to_pay(self) -> float:
        return sum(employee.to_pay() for employee in self.employees)

    def name_max_salary(self) -> str:
        max_salary_employee = max(self.employees, key=lambda emp: emp.to_pay())
        return max_salary_employee.name


def get_employees_data() -> List[Employee]:
    employees = []
    num_employees = int(input("Введіть кількість співробітників: "))

    for i in range(num_employees):
        print(f"\nВведіть дані для співробітника {i+1}:")
        emp_type = input("Тип співробітника (1 - Employee, 2 - SalesPerson, 3 - Manager): ")
        name = input("Прізвище: ")
        salary = float(input("Зарплата: "))

        if emp_type == '1':
            employees.append(Employee(name, salary))
        elif emp_type == '2':
            percent = float(input("Відсоток виконання плану: "))
            employees.append(SalesPerson(name, salary, percent))
        elif emp_type == '3':
            client_amount = int(input("Кількість обслуговуваних клієнтів: "))
            employees.append(Manager(name, salary, client_amount))

    return employees

employees = get_employees_data()
company = Company(employees)

company_bonus = float(input("\nВведіть розмір бонусу для всіх співробітників: "))
company.give_everybody_bonus(company_bonus)

total_pay = company.total_to_pay()
print(f"\nЗагальна сума заробітної плати всіх співробітників (з бонусами): {total_pay}")

max_salary_name = company.name_max_salary()
print(f"Співробітник з максимальною зарплатою (з бонусами): {max_salary_name}")
