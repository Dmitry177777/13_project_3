from data.class_node_stack import Stack

class EmptyStackException(Exception):
    pass


class Node():
    """"Класс узла"""

    def __init__(self, element=None, next_node=None):
        self.data = element
        self.next_node = next_node

class Queue():
    """"Класс СТЭКА 2"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        self.head = Node(data, self.top)
        self.tail =
        self.size += 1

    def pop(self):
        if self.head:
            val = self.head.data
            self.top = self.head.next_node
            self.size -= 1
            return val
        else:
            raise EmptyStackException
