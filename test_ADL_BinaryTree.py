import unittest
from ADL_BinarySearchTree import *

class Base_ADL_BinaryTree_tests(unittest.TestCase):

    def test_binaryTree_traversal(self):
        node1 = ADL_BinaryTree(1)
        node3 = ADL_BinaryTree(3)
        node5 = ADL_BinaryTree(5)
        node7 = ADL_BinaryTree(7)

        node2 = ADL_BinaryTree(2, node1, node3)
        node6 = ADL_BinaryTree(6, node5, node7)

        node4 = ADL_BinaryTree(4, node2, node6)

        root = node4

        self.assertEqual(list(root.breadthFirst), [4, 2, 6, 1, 3, 5, 7])

        self.assertEqual(list(root.preOrder), [4, 2, 1, 3, 6, 5, 7])

        self.assertEqual(list(root.inOrder), [1, 2, 3, 4, 5, 6, 7])

        self.assertEqual(list(root.outOrder), [7, 6, 5, 4, 3, 2, 1])

        self.assertEqual(list(root.postOrder), [1, 3, 2, 5, 7, 6, 4])

        self.assertEqual(list(root), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(list(reversed(root)), [7, 6, 5, 4, 3, 2, 1])



if __name__ == '__main__':
    unittest.main()