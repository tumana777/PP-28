import os

# if not os.path.exists('test1'):
#     os.mkdir('test1')
# else:
#     print('test folder already exists')

# print(os.listdir())

# print(os.getcwd())

# if os.path.exists('test'):
#     os.rmdir('test')
# else:
#     print("folder doesn't exist")

# if os.path.exists('test.txt'):
#     os.remove('test.txt')
# else:
#     print("file doesn't exist")

# if os.path.exists('test1'):
#     os.rmdir('test1')
# else:
#     print("folder doesn't exist")

import shutil

# if os.path.exists('test1'):
#     shutil.rmtree('test1')
# else:
#     print("folder doesn't exist")

# if os.path.exists('../Lecture 12'):
#     shutil.rmtree('../Lecture 12')
# else:
#     print("folder doesn't exist")


# with open('test.txt', 'w+') as file:
#     file.write('30')
#
#     print(file.readable())

# name = "Bob"
#
# binary_name = name.encode()
#
# print(binary_name)

# print(type(binary_name))

# with open('test.txt', 'wb') as file:
#     file.write(binary_name)


# name = "ოთარ"
#
# encoded_name = name.encode('utf-8')

# print(encoded_name)


# with open('test.bin', 'wb') as f:
#     f.write(encoded_name)

# with open('satesto.txt', 'a') as file:
#     file.write("test")

# with open('test.bin', 'rb') as file:
#     data = file.read()
#
#     print(data)


# with open('subaru.jpg', 'rb') as f:
#     print(f.read())

# import csv

# with open('companies.csv', 'r') as file:
#     reader = csv.reader(file)
#
#     for row in reader:
#         print(row)

# names = [
#     ['Bob', '25'],
#     ['John', '30'],
#     ['Walter', '65'],
# ]

# with open('test.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#
#     writer.writerow(["Name", "Age"])
#
#     writer.writerows(names)


# with open('companies.csv', 'r') as file:
#     reader = csv.DictReader(file)
#
#     for row in reader:
#         print(row)

import csv

persons = [
    {'name': "Nino", "age": 25},
    {'name': "Alex", "age": 35},
    {'name': "Levan", "age": 45},
    {'name': "Ana", "age": 23},
]

headers = ['name', 'age']

with open('persons.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)

    writer.writeheader()

    writer.writerows(persons)

import faker

fake = faker.Faker()

print(fake.first_name(), fake.last_name(), fake.city(), fake.state())
















