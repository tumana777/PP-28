# text = input("Enter text: ")
#
# longest_word = ""
#
# for word in text.split():
#     if len(word) > len(longest_word):
#         longest_word = word
#
# print(f"Longest word: {longest_word}")

# word1 = input("Enter word 1: ").lower()
# word2 = input("Enter word 2: ").lower()
#
# if len(word1) != len(word2):
#     print("Words are not anagrams")
# else:
#     for char in word1:
#         if char in word2:
#             word2 = word2.replace(char, "", 1)
#         else:
#             print("Words are not anagrams")
#             break
#     else:
#         print("Words are anagrams")

# names = ["Bob", "Alice", "John", "Ann", "Mary", "Eve", "Jane"]
#
# ages = [20, 21, 19, 30, 22, 25 , 23]
#
# countries = ["USA", "USA", "USA", "UK", "UK", "UK", "UK"]
#
# for i in range(len(names)):
#     print(f"{names[i]} is {ages[i]} years old and lives in {countries[i]}")


# names = {
#     "Bob": 20,
#     "Alice": 21,
#     "John": 19,
#     "Ann": 30,
#     "Mary": 22,
#     "Eve": 25,
#     "Jane": 23
# }

# print(type(names))

# print(names["Bob"])
#
# print(names["bob"])

# print(names.get("bob", "Not found"))

# print("Hello World")

# names["Bob"] = 25

# print(names)

# student = {
#     "name": "Bob",
#     "age": 20,
#     "country": "USA",
#     "grades": [50, 60, 70],
#     "is_active": True,
#     "pay": 1200.00
# }

# for key in student:
#     print(student[key])

# for grade in student["grades"]:
#     print(grade)

# print(student["grades"][1])

# student.clear()

# keys = list(student.keys())
# values = list(student.values())

# print(keys)
# print(values)

# print(list(student.items()))

# for key, value in student.items():
#     print(key, value)

# student.pop("country")
# student.popitem()

# student.update({"age": 25})
# student.update({"last_name": "Tumanishvili"})

# student.setdefault("age", 25)
# student.setdefault("last_name", "Tumanishvili")

# print(student)


# fruits = ["apple", "banana", "orange", "grape", "mango", "pineapple", "strawberry"]
#
# my_fruits = dict.fromkeys(fruits, 1)
#
# print(my_fruits)


# test_dict = {
#     "name": "Bob",
#     1: "age",
#     True: "is_active",
#     3.14: "pi",
# }
#
# print(test_dict)


# nums = {f"name-{i}": f"test-{i}" for i in range(1, 6)}
# nums = {i:i for i in range(1, 11) if i % 2 == 0}


# print(nums)


# products = {
#     'electronics': {
#         'laptops': {
#             1: {"name": "HP", "price": 1000},
#             2: {"name": "Lenovo", "price": 1500},
#             3: {"name": "Macbook", "price": 1200}
#         }
#     }
# }


# print(products["electronics"])
# print(products["electronics"]["laptops"])
# print(products["electronics"]["laptops"][3])
# print(products["electronics"]["laptops"][3]["price"])

# print(type(products["electronics"]["laptops"][3]["price"]))