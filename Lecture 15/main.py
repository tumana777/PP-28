# class Student:
#     is_active = True
#     pay = 1000
#     total_students = 0
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         Student.total_students += 1
#
#     def get_email(self, domain):
#         return f"{self.first_name}_{self.last_name}@{domain}"
#
# student1 = Student("Vaniko", "Khokhobashvili", 25)
# student2 = Student("Giorgi", "Gabedava", 18)
#
# print(student1.get_email("yahoo.com"))
# print(student2.get_email("gmail.com"))

# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0
#
#     def accelerate(self, s):
#         self.speed += s
#         return f"Speed is now {self.speed}"
#
#     def slow_down(self, s):
#         self.speed -= s
#         return f"Speed is now {self.speed}"
#
#     def brake(self):
#         self.speed = 0
#         return "Vehicle stopped."
#
# class SUV(Vehicle):
#     def offroading(self):
#         return f"{self.make} {self.model} can offroading."
#
# class Truck(Vehicle):
#
#     def __init__(self, make, model, year, max_weight):
#         super().__init__(make, model, year)
#         self.max_weight = max_weight
#
#     def get_max_weight(self):
#         return f"{self.make} {self.model} can get {self.max_weight}."
#
#     def transit(self):
#         return f"{self.make} {self.model} can take container."
#
# subaru = SUV("Subaru", "Forester", 2020)
# truck = Truck("Volvo", "TDX", 2021, 2500)
#
# print(subaru.accelerate(25))
# print(subaru.accelerate(25))
# print(subaru.slow_down(15))
# print(subaru.offroading())
# print(subaru.accelerate(25))
# print(subaru.slow_down(20))
# print(subaru.brake())
# print(subaru.speed)
#
# print(truck.accelerate(25))
# print(truck.accelerate(25))
# print(truck.slow_down(15))
# print(truck.transit())
# print(truck.accelerate(25))
# print(truck.slow_down(20))
# print(truck.brake())
# print(truck.speed)
# print(truck.get_max_weight())


# class Shape:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height
#
# class Rectangle(Shape):
#     def calculate_area(self):
#         return f"Rectangle area is {super().calculate_area()}"
#
# rect = Rectangle(10, 5)
# print(rect.calculate_area())
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def calculate_area(self):
#         return f"Square area is {self.side * self.side}"
#
# square = Square(15)
# print(square.calculate_area())
#
# class Triangle(Shape):
#     def calculate_area(self):
#         return f"Triangle area is {self.width * self.height * 0.5}"
#
# triangle = Triangle(10, 5)
# print(triangle.calculate_area())

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     @abstractmethod
#     def calculate_area(self):
#         return self.width * self.height
#
#     def test(self):
#         return "This is test"
#
# class Rectangle(Shape):
#     def calculate_area(self):
#         return f"Rectangle area is {super().calculate_area()}"
#
#     def get_perimeter(self):
#         return f"Rectangle perimeter is {(self.width + self.height) * 2}"
#
#
# rect = Rectangle(10, 5)
# print(rect.calculate_area())
# print(rect.get_perimeter())


# class Student:
#     is_active = True
#     pay = 1000
#     total_students = 0
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         Student.total_students += 1
#
#     def get_email(self, domain):
#         return f"{self.first_name}_{self.last_name}@{domain}"
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#
# student1 = Student("Vaniko", "Khokhobashvili", 25)
# student2 = Student("Giorgi", "Gabedava", 18)
#
# print(student1)
# print(student2)