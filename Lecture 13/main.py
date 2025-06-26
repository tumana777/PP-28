# import csv, faker, random
#
# fake = faker.Faker()
#
# headers = ["ID", "first_name", "last_name", "age"]
#
# with open('persons.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=headers)
#     writer.writeheader()
#
#     persons = [
#         {
#             "ID": i,
#             "first_name": fake.first_name(),
#             "last_name": fake.last_name(),
#             "age": random.randint(20, 80),
#         }
#         for i in range(1, 51)
#     ]
#
#     writer.writerows(persons)

    # for i in range(1, 51):
    #     writer.writerow(
    #         {
    #             "ID": i,
    #             "first_name": fake.first_name(),
    #             "last_name": fake.last_name(),
    #             "age": random.randint(20, 80),
    #         }
    #     )

# with open('persons.txt', 'r') as f, open('under_50.txt', 'w') as file1, open('over_50.txt', 'w') as file2:
#     persons = f.readlines()
#
#     for person in persons:
#         age = int(person.split(', ')[1])
#
#         if age < 50:
#             file1.write(person)
#         else:
#             file2.write(person)


# person = "Dr. Briana Davidson, 22, South Hunterside"
#
# splitted = person.split(', ')
#
# print(splitted)