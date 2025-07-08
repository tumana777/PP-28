# class MyClass:
#
#     def __new__(cls):
#         print("Called __new__ method")
#         return super().__new__(cls)
#
#     def __init__(self):
#         print("Called __init__ method")
#
# obj = MyClass()

# class MyMeta(type):
#     def __new__(cls, name, bases, attrs):
#         print(name)
#         print(bases)
#         print(attrs)
#         return super().__new__(cls, name, bases, attrs)
#
# class A:
#     pass
#
# class MyClass(A, metaclass=MyMeta):
#     test = "Hello"
#
#     def satesto(self):
#         pass
#
# obj = MyClass()

# class MyMeta(type):
#     def __new__(cls,  name, bases, attrs):
#         attrs["created_by"] = "Admin"
#         return super().__new__(cls, name, bases, attrs)
#
# class Test(metaclass=MyMeta):
#     pass
#
# class Test2(metaclass=MyMeta):
#     pass
#
# obj = Test
#
# obj1 = Test2
#
# print(obj.created_by)
# print(obj1.created_by)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def delete(self, data):
        current = self.head

        if current and current.data == data:
            self.head = current.next
            current = None
            return

        prev = None

        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

    # 8 -> 5 -> 7 -> 6 -> 9 ->

    def print_data(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

ll = LinkedList()

# print(ll.head)

ll.append(8)
ll.append(5)
ll.append(7)
ll.append(6)
ll.append(9)

print(ll.head.data)

ll.print_data()
print()

# ll.prepend(15)

ll.print_data()
print()

# print(ll.head.data)

# 8 -> 5 -> 7 -> 6 -> 9 ->

ll.delete(7)

ll.print_data()
print()