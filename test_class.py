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

        self.list1 = ap.LinkedList()
        self.list1.insert_beginning({'id': 7, 'username': 'lazzy508509'})
        self.list1.insert_at_end({'id': 6, 'username': 'mik.roz'})
        self.list1.insert_at_end({'id': 5, 'username': 'mosh_s'})
        self.list1.insert_beginning({'id': 4, 'username': 'serebro'})

    def test_list_print_ll(self):
        ll_string: str = " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"
        assert self.list.print_ll() == ll_string

    def test_list_to_list(self):
        ll_list = [{'id': 4, 'username': 'serebro'},
                   {'id': 7, 'username': 'lazzy508509'},
                   {'id': 6, 'username': 'mik.roz'},
                   {'id': 5, 'username': 'mosh_s'}]

        assert str(self.list1.to_list()) == str(ll_list)

    def test_list_get_data_by_id(self):
        assert str(self.list1.get_data_by_id(4)) == str({'id': 4, 'username': 'serebro'})
        assert str(self.list1.get_data_by_id(7)) == str({'id': 7, 'username': 'lazzy508509'})
        assert str(self.list1.get_data_by_id(6)) == str({'id': 6, 'username': 'mik.roz'})
        assert str(self.list1.get_data_by_id(5)) == str({'id': 5, 'username': 'mosh_s'})


if __name__ == '__main__':
    unittest.main()
