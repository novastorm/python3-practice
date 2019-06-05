import unittest
from ADL_BinaryTree import *

class Base_ADL_BinaryTree_tests(unittest.TestCase):

    def test_binary_tree_initialization(self):
        with self.assertRaises(TypeError):
            node = ADL_BinaryTree()

        node_2 = ADL_BinaryTree(2)
        self.assertEqual(node_2.value, 2)
        self.assertIsNone(node_2.left)
        self.assertIsNone(node_2.right)

        node_7 = ADL_BinaryTree(7)
        self.assertEqual(node_7.value, 7)
        self.assertIsNone(node_7.left)
        self.assertIsNone(node_7.right)

        node_2plus7 = ADL_BinaryTree('+',  node_2, node_7)
        self.assertEqual(node_2plus7.value, '+')
        self.assertEqual(node_2plus7.left.value, node_2.value)
        self.assertEqual(node_2plus7.right.value, node_7.value)


if __name__ == '__main__':
    unittest.main()