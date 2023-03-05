from data.class_node_stack import Node
from data.class_node_stack import Stack

n1 = Node(5)
n2 = Node('a')
print(n1.data)
print(n2.data)
print(n1)
print(n2.next_node)

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')
print(stack.top.data)
print(stack.top.next_node.data)
print(stack.top.next_node.next_node.data)
print(stack.top.next_node.next_node.next_node)
print(stack.top.next_node.next_node.next_node.data)
