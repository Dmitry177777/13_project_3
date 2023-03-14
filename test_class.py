import unittest

import data.class_node_stack as am


# import data.custom_queue as at

class TestStack(unittest.TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.names = ['data1',
                      'data2',
                      'data3']

    def test_init(self):
        stack = am.Stack()
        self.assertIsNone(stack.top)
        self.assertEqual(stack.size, 0)

    def test_push(self):
        stack = am.Stack()
        for name in self.names:
            stack.push(name)

        names = list(self.names)
        names.reverse()

        # self.assertEqual(names.__str__(), stack.__str__())
        # self.assertEqual(len(names), stack.size)


if __name__ == '__main__':
    unittest.main()
