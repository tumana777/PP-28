import json

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f'Person({self.name}, {self.age})'

# p1 = Person('John', 20)
#
# def person_serializer(obj):
#     return {"name": obj.name, "age": obj.age}

# print(person_serializer(p1))

# with open('person.json', 'w') as f:
#     json.dump(p1, f, default=person_serializer, indent=4)

# def person_deserializer(obj):
#     return Person(obj['name'], obj['age'])
#
# with open('person.json', 'r') as file:
#     person = json.load(file, object_hook=person_deserializer)
#
#
# print(person)

import pickle

# cars = ['BMW', 'Subaru', 'Mercedes']

# serialized_cars = pickle.dumps(cars)

# print(serialized_cars)

# deserialized_cars = pickle.loads(serialized_cars)
#
# print(deserialized_cars)

# with open('cars.pkl', 'wb') as f:
#     pickle.dump(cars, f)


# with open('cars.pkl', 'rb') as f:
#     cars_data = pickle.load(f)
#
# print(cars_data)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f'Person({self.name}, {self.age})'
#
# p1 = Person('John', 20)
#
# with open("person.pkl", "wb") as f:
#     pickle.dump(p1, f)

#
# with open('person.pkl', 'rb') as file:
#     person = pickle.load(file)

# print(person)














