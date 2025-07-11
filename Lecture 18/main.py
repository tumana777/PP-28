# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.size = 0
#
#     def empty(self):
#         return self.size == 0
#
#     def peek(self):
#         if self.empty():
#             return "Stack is empty"
#         return self.top.data
#
#     def push(self, data):
#         new_node = Node(data)
#
#         new_node.next = self.top
#         self.top = new_node
#         self.size += 1
#
#     def pop(self):
#
#         if self.empty():
#             return "Stack is empty"
#
#         # popped_element = self.top.data
#
#         self.top = self.top.next
#         self.size -= 1
#         # return popped_element
#
# stack = Stack()

# print(stack.top)
# print(stack.size)
# print(stack.empty())
# print(stack.peek())

# stack.push(6)
# stack.push(9)
# stack.push(4)
# stack.push(5)
#
# print(stack.peek())
#
# print(stack.pop())
# print(stack.pop())
#
# print(stack.peek())

# from collections import deque
#
# q = deque(maxlen=4)
#
# q.append(6)
# q.append(2)
# q.append(7)
# q.append(9)
# q.append(10)
#
# print(q.pop())
# print(q.popleft())

# print(q.pop())
# print(q.popleft())

# q.appendleft(5)
#
# print(q.popleft())

# from queue import Queue
#
# q = Queue(maxsize=3)
# q.put(6)
# q.put(8)
# q.put(4)

# print(q.full())

# q.put_nowait(7)
# q.put_nowait(7)

# print(q.queue)
#
# q.get()
# q.get()
# q.get()
# q.get()
# q.get()
#
# print(q.queue)

# print(q.get_nowait())
# print(q.get_nowait())
# print(q.get_nowait())
# print(q.get_nowait())
# print(q.get_nowait())


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None


    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _print_parents(self, node, parent):
        if node:
            if parent is None:
                print(node.key, "-> Root")
            else:
                print(node.key, "-> ", parent.key)

            self._print_parents(node.left, node)
            self._print_parents(node.right, node)

    def print_parents(self):
        print("Parents are: ")
        self._print_parents(self.root, None)

                                        #       9
                                        # 8           12
                                        #           10
bst = BST()

bst.insert(9)
bst.insert(12)
bst.insert(8)
bst.insert(10)

bst.print_parents()
















