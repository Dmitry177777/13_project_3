class EmptyStackException(Exception):
    pass


class Node():
    """"Класс узла"""

    def __init__(self, element=None, next_node=None):
        self.data = element
        self.next_node = next_node


class Stack():
    """"Класс СТЭКА"""

    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = 0
    def is_full(self):
        "«Определить, заполнена ли очередь»"
        if (self.tail + 1) % self.size == self.head:
            return True
        return False

    def enqueue(self, data):
        self.head = Node(data, self.top)
        self.tail = (self.tail+1) % self.size
        self.size += 1

    def pop(self):
        if self.head:
            val = self.head.data
            self.top = self.head.next_node
            self.size -= 1
            return val
        else:
            raise EmptyStackException

