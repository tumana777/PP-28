# persons = [
#     ('Kelly', 'Simpson', 26),
#     ('Erika', 'Stephens', 24),
#     ('Cheryl', 'Dunn', 30),
#     ('Amy', 'Larsen', 49),
#     ('Christine', 'Gordon', 23),
#     ('Monica', 'Huff', 38),
#     ('David', 'Nixon', 36),
#     ('Cindy', 'Escobar', 41),
#     ('Cindy', 'White', 33),
#     ('Joel', 'Hall', 43),
#     ('Steven', 'Winters', 28),
#     ('Alex', 'Cole', 68),
#     ('Alex', 'Smith', 32),
#     ('Alex', 'Down', 52),
#     ('Brittany', 'Thompson', 18),
#     ('Ernest', 'Young', 43),
#     ('Traci', 'Wells', 38),
#     ('Andrew', 'Flores', 61),
#     ('Christopher', 'Lewis', 29),
#     ('Kevin', 'Willis', 57),
#     ('Kayla', 'Lucas', 28),
#     ('Michelle', 'Rush', 43),
#     ('Thomas', 'Mason', 37)
# ]
#
#
# while True:
#     first_name = input('Please enter first name: ').lower()
#
#     if first_name == "stop":
#         break
#
#     found_persons = [person for person in persons if person[0].lower() == first_name]
#
#     print(found_persons)
#
#     if not found_persons:
#         print("This first name doesn't exist in the list.")
#     else:
#         last_name = input('Please enter last name: ').lower()
#
#         for person in found_persons:
#             if person[1].lower() == last_name:
#                 print(f"{person[0]} {person[1]} is {person[2]} years old.")
#                 break
#         else:
#             print("Last name not found")
from pyexpat.errors import messages


# text = input("Please input text: ")
#
# lst = []

# for i in text:
#     if i != " ":
#         lst.append(i)

# text = text.replace(" ", "")

# print(tuple(lst))


# def add(a, b):
#     return a + b
#
# add(1, 2)

# def add(n, m, *args):
#     total = 0
#
#     for i in args:
#         total += i
#
#     return total

# print(add(1, 2, 4, 6, 2))
# print(add(1, 2, 6, 2))

# add(3, 4, 5, 7, 9)

# def add(*args):
#     print(args)
#
# x = input("enter something: ")
#
# add()

#
# def add(a, b):
#     return a + b
#
# lst = [3, 5]
#
# print(add(*lst))

# def add(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
# lst = [3, 5]
#
# add(*lst, 8)

# def greeting(name="Guest"):
#     return f"Hello {name}"

# print(greeting())
# print(greeting("World!"))

# def add(a, b):
#     print(f"a = {a}, b = {b}")
#
# add(b=3, a=1)


# def greet(name, age, message="Hello"):
#     print(f"name: {name}, message: {message}, age: {age}")
#
# greet("John", message="Hi", age=25)


# def greet(**kwargs):
#     return kwargs
#
# print(greet(name="luka", message="Hello", age=25))

# def greet(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# greet("test", "test2", name="luka", message="Hello", age=25)


# x = "Global Variable"
#
# def outer():
#     x = "Enclosing Variable"
#
#     def inner():
#         x = "Local Variable"
#
#         print(x)
#
#     inner()
#
#
# outer()


# def test():
#     x = 4
#     return x
#
# print(x)