# lst = [4, 9, 8, 12, 6, 7, 5, 9]
#
# jami = 0
#
# for item in lst:
#     jami += item
#
# length = 0
#
# for _ in lst:
#     length += 1
#
# print(jami / length)

# lst = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
#
# new_lst = []
#
# for item in lst:
#     if item not in new_lst:
#         new_lst.append(item)
#
# print(new_lst)

# empty_tuple = ()
# print(type(empty_tuple))

# my_tuple = (1, 2, 3, 5, 7, 2, 1, 8, 4)
# print(len(my_tuple))
# print(my_tuple[0])
# print(my_tuple[1:7])
# print(my_tuple[::-1])
# print(my_tuple[-1])

# for item in my_tuple:
#     print(item)


# lst = ["Hello", 1, True, [2, 7], 3.14, 5, 6]
#
# tuple1 = tuple(lst)

# print(tuple1)

# lst[2] = False
# print(lst)

# tuple1[2] = False

# print(tuple1)
# tuple1[3][1] = 5
#
# print(tuple1)

# my_tuple = ("Hello")
# print(type(my_tuple))

# my_tuple = ("Hello", )
# print(type(my_tuple))


# lst = ["Hello", 1, True, [2, 7], 3.14, 5, 6]
#
# for i, value in enumerate(lst):
#     print(i, value)

# tuple1 = (2, 5, 3)
#
# n1, n2, n3 = tuple1
#
# print(n1)
# print(n2)
# print(n3)


# tuple1 = (2, 5, 3, 7, 6)
#
# n1, *n2, n3 = tuple1
#
# print(n1)
# print(n2)
# print(n3)

# tuple3 = 5, 3, 6, 3, 4, 7, 6, "Hi"
# print(type(tuple3))

# tuple1 = (2, 5, 3, 7, 6)
#
# my_dict = {
#     tuple1: "test",
#     "name": "Otar"
# }
#
# print(my_dict)


# my_set = set()
#
# print(type(my_set))

# my_set = {5, 3, 6, 3, 4, 7, 6}
# print(type(my_set))

# my_set1 = {2, True, 7.15, "Hello"}

# print(my_set1)

# lst = [5, 3, 6, 3, 4, 7, 6]
#
# my_set1 = set(lst)


# my_set = {5, 3, 6, 3, 4, 7, 6}
# print(my_set)

# set1 = {5, 6, 3, 4, 7}
# set2 = {8, 1, 3, 6, 9}
#
# fruits = {"banana", 4, "apple", "cherry"}
# fruits.pop()
# fruits.remove("banana")

# print(fruits)


# set1.add(2)
# set1.pop()
# print(set1)

# print(set1.difference(set2))
# print(set1 - set2)

# print(set1.intersection(set2))
# print(set1 & set2)

# print(set1.symmetric_difference(set2))
# print(set1 ^ set2)

# print(set1.union(set2))
# print(set1 | set2)

# set1.update(set2)

# set1 = {5, 6, 3, 4, 7}
# my_frozen = frozenset(set1)
#
# print(my_frozen)