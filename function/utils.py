from data.class_node_stack import Stack

stack = Stack()
stack.push('data1')
data = stack.pop()

# стэк стал пустой
print(stack.top)
# None

# pop() удаляет элемент и возвращает данные удаленного элемента
print(data)
# 'data1'


stack = Stack()
stack.push('data1')
stack.push('data2')
data = stack.pop()

# теперь последний элемента содержит данные data1
print(stack.top.data)
# 'data1'

# данные удаленного элемента
print(data)
#'data2'
