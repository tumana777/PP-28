# def add(x, y):
#     return x + y
#
# result = add(5, 6)
#
# print(result)

# def test(func, a, b):
#     return func(a, b)
#
# def add(x, y):
#     return x + y
#
# def sub(x, y):
#     return x - y
#
# print(test(add, 3, 4))
# print(test(sub, 3, 4))

# def get_multiplier(a):
#     def multiplier(b):
#         return a * b
#     return multiplier
#
# multiplier_by_5 = get_multiplier(5)
# multiplier_by_7 = get_multiplier(7)

# print(multiplier_by_5(9))
# print(multiplier_by_5(6))

# print(multiplier_by_7(9))
# print(multiplier_by_7(6))


# def find_factorial(x):
#     print(x)
#     if x == 0 or x == 1:
#         return 1
#     return x * find_factorial(x - 1) # 5 x 4 x 3 x 2 x 1
#
# print(find_factorial(5))


# test = lambda x: x
#
# print(test('hello'))


# add = lambda x, y: x + y
#
# print(add(8, 9))

# def my_function(n):
#     return len(n)


# names_lst = ["nodar", "levan", "nikoloz", "lasha", "giorgi", "nino", "ani"]


# lens = list(map(lambda x: len(x), names_lst))
#
# print(lens)

# capitalized_names = list(map(lambda x: x.capitalize(), names_lst))
#
#
# print(capitalized_names)


# names_lst = ["nodar", "levan", "nikoloz", "lasha", "giorgi", "nino", "ani", "aleksandre"]

# def long_names(x):
#     return len(x) > 5

# long_name_list = tuple(filter(lambda a: len(a) > 5, names_lst))
#
# print(long_name_list)

# names_lst = ["nodar", "levan", "nikoloz", "lasha", "giorgi", "nino", "ani", "aleksandre"]
#
# age_list = [25, 36, 75, 54, 25, 23, 21, 46]
#
# cities = ["tbilisi", "Kutaisi", "Batumi", "Zugdidi", "Rustavi", "Akhalcikhe"]
#
# print(list(zip(names_lst, age_list, cities)))

# from functools import reduce
#
# def add(a, b):
#     return a + b
#
# numbers = [25, 30, 75, 20, 25, 23, 20, 22]
#
# result = reduce(add, numbers)
#
# print(result)


# number = int(input("Enter a number: "))
#
# print(number)
#
# print("End of program")


try:
    num1 = int(input("Please input num1: "))
    num2 = int(input("Please input num2: "))

    result = num1 / num2
except ValueError:
    print("Invalid integer")
except ZeroDivisionError:
    print("Division by zero")
except Exception as e:
    print(e)
else:
    print(result)
finally:
    print("End of program")