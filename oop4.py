# inheritance
class Employee:
    def __init__(self, name, email, department, salary):
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary

    def show_details(self):
        print(self.name, self.email, self.department, self.salary)


class PermanentEmployee(Employee):  # inheriting
    def __init__(self, name, email, department, salary, cover, increment):
        super().__init__(name, email, department, salary)
        self.cover = cover
        self.increment = increment


class ContractEmployee(Employee):
    def __init__(self, name, email, department, salary, tenure):
        super().__init__(name, email, department, salary)
        self.tenure = tenure
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Contract Length: {self.tenure}")

p1 = PermanentEmployee("Jane Maek", "jm@yahoo.com", "HR", 100_000, "Britam", 1000)
c1 = ContractEmployee("Jin Jung", "jj@gmail.com", "Sales", 88_000, 3)

p1.show_details()
c1.show_details()
