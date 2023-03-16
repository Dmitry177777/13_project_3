import unittest

import data.class_node_stack as am
import data.custom_queue as at


class TestStack(unittest.TestCase):
    stack = am.Stack()
    node = am.Node()
    queue = at.Queue()

    names = [
        'data1',
        'data2',
        'data3'
    ]

    # def test_init(self):
    #     self.assertIsNone(node.data)

    def test_push(self):
        for name in TestStack.names:
            TestStack.stack.push(name)

        # self.assertEqual(TestStack.node.data[1], TestStack.names[2])
        # self.assertEqual(TestStack.node.data[2], TestStack.names[1])
        # self.assertEqual(TestStack.node.data[3], TestStack.names[0])

    # def test_init(self):
    #
    #     self.assertIsNone(self.stack.top)
    #     self.assertEqual(self.stack.size, 0)

    # def test_push(self):
    #     self.assertEqual(self.stack.top, self.node.data)
    #
    #
    #
    #     self.assertEqual(names, self.node.data.__repr__())
    #     self.assertEqual(len(names), self.stack.size)

    # def test_init(self):
    #     # queue = at.Queue()
    #     self.assertIsNone(queue.head)
    #     self.assertIsNone(queue.tail)
    #     self.assertEqual(queue.length, 0)
    #
    # def test_enqueue(self, elem):
    #     # queue = at.Queue()
    #     tmp = Node(elem)
    #     for name in self.names:
    #         queue.push(name)
    #
    #     names = list(self.names)
    #     names.reverse()
    #
    #     self.assertEqual(names.__str__(), stack.__str__())
    #     self.assertEqual(len(names), stack.size)
    #
    # def enqueue(self, elem):
    #     "Операция входа"
    #
    #     tmp = Node(elem)
    #     if self.is_empty():
    #         self.head = tmp
    #         self.tail = tmp
    #     else:
    #         self.tail.next_node = tmp
    #         self.tail = tmp
    #     self.length += 1


if __name__ == '__main__':
    unittest.main()
