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
#     def __repr__(self):
#         return f"Student({self.first_name}, {self.last_name}, {self.age})"
#
# student1 = Student("Vaniko", "Khokhobashvili", 25)
# student2 = Student("Giorgi", "Gabedava", 18)
#
# print(student1)
# print(student2)
# print(student1.__repr__())
# print(student2.__repr__())
#
#
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         if isinstance(other, Vector):
#             if isinstance(self.x, int) and isinstance(other.x, int):
#                 return Vector(self.x + other.x, self.y + other.y)
#             return "x is not a number"
#         return "This object is not a Vector"
#
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
#
# vector1 = Vector(1, 2)
# vector2 = Vector(3, 4)
#
# print(vector1 + vector2)


# class Student:
#     pay = 1000
#     discount = 0.8
#
#     def __init__(self, name, age, pay, discount):
#         self.name = name
#         self.age = age
#         self.pay = pay
#         self.discount = discount
#
#     def get_pay(self):
#         return self.pay * self.discount
#
#     @classmethod
#     def get_student_pay(cls):
#         return cls.pay * cls.discount
#
#     @staticmethod
#     def get_resting():
#         day = input("Enter weekday: ").lower()
#
#         if day == "sunday":
#             return "You can rest today"
#         return "You can't rest today"
#
# student1 = Student("John", "25", 800, 0.7)
# print(student1.get_pay())
# print(student1.get_student_pay())
# print(student1.get_resting())



# class Student:
#     def __init__(self, name, age, pay):
#         self.name = name
#         self._age = age
#         self.__pay = pay
#
#     def get_age(self):
#         return self._age
#
#     @property
#     def pay(self):
#         return self.__pay
#
#     @pay.setter
#     def pay(self, value):
#         self.__pay = value
#
#
# student1 = Student("John", 25, 1000)

# print(student1.name)
# print(student1._age)

# student1._age = 30

# print(student1.get_age())
# print(student1.name)

# print(student1.__pay)

# student1.__pay = 1500
#
# print(student1.pay)
# student1.pay = 1200
# print(student1.pay)


# class Multiplier:
#     def __init__(self, a):
#         self.a = a
#
#     def __call__(self, b):
#         return self.a * b
#
# double = Multiplier(2)
# triple = Multiplier(3)
#
# print(double.__call__(2))
# print(triple(3))

# def test():
#     print("Test")
#
# test.__call__()

# def change_value(func):
#     def wrapper(*args, **kwargs):
#         a = args[0] + 2
#         b = args[1] + 3
#         return func(a, b)
#     return wrapper
#
#
# @change_value
# def print_numbers(x, y):
#     return f"x: {x}, y: {y}"
#
#
# print(print_numbers(4, 7))

# import time
#
# def time_decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Function work took {end - start} seconds.")
#         return result
#     return wrapper


# def test():
#     start = time.time()
#     print("Started function execution...")
#     time.sleep(1)
#     print("Finished function execution.")
#     end = time.time()
#     print(f"Function work took {end - start} seconds.")

# test()

# @time_decorator
# def test():
#     time.sleep(2)
#
# test()
#
# @time_decorator
# def print_hello():
#     for _ in range(900):
#         print("Hello World!")
#
# print_hello()