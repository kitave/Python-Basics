class Person:
    # constructor
    def __init__(self, name, dob, color, weight, height):
        self.name = name
        self.dob = dob
        self.color = color
        self.weight = weight
        self.height = height

    def display(self):
        print(f"Name is {self.name} and dob is {self.dob}")

    def get_bmi(self):
        result = self.weight / self.height ** 2
        return round(result, 2)


# blueprint for creating objects
p1 = Person("Hun Chink", "18-1-2006", "Black", 53.5, 1.75)
p2 = Person("Edward", "12-20-2011", "white", 60.3, 1.35)
p3 = Person("Jalon", "23-0-2005", "White", 60.4, 2.34)

p1.display()
p2.display()

print(p1.get_bmi())  # use ctrl + D to duplicate sentence
print(p2.get_bmi())
