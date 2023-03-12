class EmptyStackException(Exception):
    pass


class Node():
    """"Класс узла"""

    def __init__(self, element=None, next_node=None):
        self.data = element
        self.next_node = next_node

    def __str__(self):
        if self.data:
            return self.data.__str__()
        else:
            return 'Empty Node'

    def __repr__(self):
        return self.__str__()


class Queue():
    """"Класс очереди"""

    def __init__(self):
        self.data = None
        self.head = 0
        self.tail = 0

    def enqueue(self, data):
        self.data = Node(data, self.data)
        self.tail += 1

    # def pop(self):
    #     if self.head:
    #         val = self.head.data
    #         self.head = self.head.next_node
    #         self.size -= 1
    #         return val
    #     else:
    #         raise EmptyStackException
