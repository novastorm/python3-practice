import unittest
from ADL_Stack import *

def test_base(base_cls):
    class BaseClassSkipper(base_cls):
        @classmethod
        def setUpClass(cls):
            if cls is BaseClassSkipper:
                raise unittest.SkipTest("Base class")
            super().setUpClass()
    return BaseClassSkipper

@test_base
class Base_ADL_Stack_tests(unittest.TestCase):

    def setUp(self):
        raise NotImplementedError

    def test_stack_initialization(self):
        self.assertTrue(self.stack.isEmpty)
        self.assertEqual(self.stack.count, 0)
        self.assertIsNone(self.stack.peek)


    def test_stack_push(self):
        for i in range(3):
            self.stack.push(i)
            self.assertFalse(self.stack.isEmpty)
            self.assertEqual(self.stack.peek, i)
            self.assertEqual(self.stack.count, i+1)


    def test_stack_pop(self):
        self.assertIsNone(self.stack.pop())
        for i in range(3):
            self.stack.push(i)
            self.assertEqual(self.stack.peek, i)

        for i in range(2, 0-1, -1):
            self.assertEqual(self.stack.peek, i)
            self.assertEqual(self.stack.pop(), i)
            self.assertEqual(self.stack.count, i)


class test_ADL_SinglyLinkedList_Stack(Base_ADL_Stack_tests):

    def setUp(self):
        self.stack = ADL_SinglyLinkedList_Stack()


class test_ADL_DoublyLinkedList_Stack(Base_ADL_Stack_tests):

    def setUp(self):
        self.stack = ADL_DoublyLinkedList_Stack()


class test_ADL_List_Stack(Base_ADL_Stack_tests):

    def setUp(self):
        self.stack = ADL_List_Stack()


if __name__ == '__main__':
    unittest.main()