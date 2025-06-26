# import string

# print(string.punctuation)

# def word_counter(sentence):
#     lst = sentence.lower().split()
#
#     my_dict = {}
#
#     for word in lst:
#         if word not in my_dict:
#             my_dict[word.strip(string.punctuation)] = 1
#         else:
#             my_dict[word.strip(string.punctuation)] += 1
#
#
#     return my_dict
#
# print(word_counter("This is a test. This test is fun."))

# file = open("test.txt","r")

# print(file.readable())

# data = file.read()
#
# print(data)
#
# file.close()

# file = open("../Lecture 10/main.py")
#
# print(file.read(18))
#
# file.close()
#
#
# print(file.read())

# file = open("test.txt","r")
#
# data = file.read(16)
#
# file.seek(0)
#
# new_data = file.read()

# print(data)
# print(new_data)
#
# file.close()

# file = open("test.txt","r")
#
# line1 = file.readline()
# line2 = file.readline()
#
# print(line1)
# print(line2)
#
# file.close()

# file = open("test.txt","r")

# lines = file.readlines()

# print(lines)

# for line in lines:
#     print(line)

# file.close()

# file = open("test.txt","w")

# print(file.writable())

# file.write("I love python\nI love programming")


# file.close()

# file = open("test.txt","a")
#
# file.write("\nI love gaming")
#
# file.close()

# file = open("numbers.txt","x")
#
# file.write("1\n2\n3")
#
# file.close()

# file = open("numbers.txt", "w+")
#
# print(file.writable())
# print(file.readable())
#
# file.close()


# file = open("numbers.txt", "w")
#
# numbers = ["1\n", "2\n", "3\n", "4\n", "5\n", "6\n", "7\n", "8\n", "9"]
#
# file.writelines(numbers)
#
# file.close()


with open("test.txt", "r") as file:
    print(file.read())