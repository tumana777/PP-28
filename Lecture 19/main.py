# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
# class BookManager:
#     def add_book(self):
#         title = input("Enter title: ")
#         author = input("Enter author: ")
#
#         book = Book(title, author)
#
# book_manager = BookManager()
#
#
# book_manager.add_book()

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# serialized_data = ','.join([str(num) for num in nums])
#
# print(serialized_data)
#
# with open('nums.txt', 'w') as file:
#     file.write(serialized_data)


# with open('nums.txt') as f:
#     data = f.read()
#
# # print(type(data))
#
# deserialized_data = [int(num) for num in data.split(',')]
#
# print(deserialized_data)



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f'Person({self.name}, {self.age})'
#
# p1 = Person("Bob", 25)
# p2 = Person("John", 32)

# print(p1)
# print(p2)

# def person_serializer(person):
#     return {
#         "name": person.name,
#         "age": person.age
#     }
#
# serialized_person = person_serializer(p1)
# serialized_person2 = person_serializer(p2)

# print(serialized_person)
# print(serialized_person2)

# def person_deserializer(person):
#     return Person(person["name"], person["age"])
#
# deserialized_person = person_deserializer(serialized_person)
# deserialized_person2 = person_deserializer(serialized_person2)
#
#
# print(deserialized_person)
# print(deserialized_person2)


import json
from xml.etree.ElementTree import indent

# student = {
#     'name': 'John',
#     'age': 25,
#     'gender': 'male',
#     'grades': [58, 75, 65],
#     'course': {
#         'name': 'Python',
#         'lecturer': 'Otar'
#     },
#     'status': True
# }
#
# student1 = {
#     'name': 'Bob',
#     'age': 32,
#     'gender': 'male',
#     'grades': [67, 82, 90],
#     'course': {
#         'name': 'Python',
#         'lecturer': 'Otar'
#     },
#     'status': False
# }
#
# students = [student, student1]
#
# with open('students.json', 'w') as outfile:
#     json.dump(students, outfile, indent=4)


# with open('student.json', 'r') as file:
#     json_data = json.load(file)
#
# print(type(json_data))


student = {
    'name': 'John',
    'age': 25,
    'gender': 'male',
    'grades': [58, 75, 65],
    'course': {
        'name': 'Python',
        'lecturer': 'Otar'
    },
    'status': True
}

# print(type(student))

serialized_student = json.dumps(student, indent=4)

# print(type(json_student))

# print(json_student)

deserialized_student = json.loads(serialized_student)

# print(type(deserialized_student))

print(deserialized_student)



















