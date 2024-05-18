class Dog_Bark:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print('woof woof')

dog_obj = Dog_Bark('alex', 'labra')


class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def paycheck(self):
        return self.salary/52
    

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def print_employee(self):
        for employee in self.employees:
            print(employee.name)

    def pay_employee(self):
        print('Paying ')
        for pay in self.employees:
            print('Paying ' + pay.name + ' - $' + str(pay.paycheck()))


def main():
    my_company = Company()

    employee1 = Employee('Sarah', 123, 50000)
    employee2 = Employee('Alex', 323, 70000)

    my_company.add_employee(employee1)
    my_company.add_employee(employee2)

    my_company.print_employee()
    my_company.pay_employee()

main()
