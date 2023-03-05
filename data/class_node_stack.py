class Node():
    """"Класс узла"""

    def __init__(self, element=None, next_node=None) -> 'Node':
        self.data = element
        self.next_node = next_node


class EmptyStackException(Exception):
    pass

class Stack():
    """"Класс СТЭКА"""

    def __init__(self) -> 'Stack':  # инициализируется одним атрибутом, хранящим ссылку на верхний (крайний в стэке) узел. Для пустого стэка этот атрибут будет содержать `None`.
        self.top = None
        self.size = 0
    def push(self, data) -> None:
        """Метод добавления данных в Stack"""
        self.top = Node(data, self.top)
        self.size += 1

    def top(self) -> str:
        """Метод возвращающий верхнее значениее Stack"""

        if self.top:
           return self.top.element
        else:
           raise EmptyStackException


