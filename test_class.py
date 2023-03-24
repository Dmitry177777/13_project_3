import unittest

import data.class_node_stack as am
import data.custom_queue as at
import data.linked_list as ap


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = am.Stack()
        self.stack.push('data1')
        self.stack.push('data2')
        self.stack.push('data3')

    def test_stack_push(self):
        self.assertEqual(self.stack.top.data, 'data3')
        self.assertEqual(self.stack.top.next_node.data, 'data2')
        self.assertEqual(self.stack.top.next_node.next_node.data, 'data1')


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = at.Queue()
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')

    def test_queue_enqueue(self):
        assert self.queue.head.data == 'data1'
        assert self.queue.head.next_node.data == 'data2'
        assert self.queue.tail.data == 'data3'
        assert self.queue.tail.next_node is None

    def test_queue_dequeue(self):
        assert self.queue.dequeue() == 'data1'
        assert self.queue.dequeue() == 'data2'
        assert self.queue.dequeue() == 'data3'
        assert self.queue.dequeue() == None


class LinkedList(unittest.TestCase):

    def setUp(self):
        self.list = ap.LinkedList()
        self.list.insert_beginning({'id': 1})
        self.list.insert_at_end({'id': 2})
        self.list.insert_at_end({'id': 3})
        self.list.insert_beginning({'id': 0})

    def test_list_print_ll(self):
        ll_string: str = " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"
        assert self.list.print_ll() == ll_string


if __name__ == '__main__':
    unittest.main()
