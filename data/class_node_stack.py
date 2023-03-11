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
        self.top = None
        self.size = 0

    def push(self, data):
        self.top = Node(data, self.top)
        self.size += 1

    def pop(self):
        if self.top:
            val = self.top.data
            self.top = self.top.next_node
            self.size -= 1
            return val
        else:
            raise EmptyStackException

    # def __init__(
    #         self):  # инициализируется одним атрибутом, хранящим ссылку на верхний (крайний в стэке) узел. Для пустого стэка этот атрибут будет содержать `None`.
    #     self.top = None
    #     # self.size = 0
    #
    # def isEmpty(self):
    #     return self.top is None
    #
    # def push(self, data) -> None:
    #     """Метод добавления данных в Stack"""
    #     self.top = Node(data, self.top)
    #     # self.size += 1
    #
    # # def top(self) -> str:
    # #     """Метод возвращающий верхнее значениее Stack"""
    # #
    # #     if self.top:
    # #         return self.top.element
    # #     else:
    # #         raise EmptyStackException
    #
    # def pop(self) -> str:
    #     # Remove a value from the stack and return.
    #     if self.isEmpty():
    #         raise EmptyStackException
    #     val = self.top.data
    #     self.top = self.top.nextNode
    #     # self.size -= 1
    #     return val
