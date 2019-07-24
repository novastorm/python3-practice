import unittest
from ADL_BinaryTree import *

class Base_ADL_BinaryTree_tests(unittest.TestCase):
    Node = ADL_BinaryTreeNode_Iterative

    def test_binaryTree_traversal(self):
        node1 = self.Node(1)
        node3 = self.Node(3)
        node5 = self.Node(5)
        node7 = self.Node(7)

        node2 = self.Node(2, node1, node3)
        node6 = self.Node(6, node5, node7)

        node4 = self.Node(4, node2, node6)

        root = node4

        self.assertEqual(len(root), 7)

        self.assertEqual(list(root.breadthFirst), [4, 2, 6, 1, 3, 5, 7])

        self.assertEqual(list(root.preOrder), [4, 2, 1, 3, 6, 5, 7])

        self.assertEqual(list(root.inOrder), [1, 2, 3, 4, 5, 6, 7])

        self.assertEqual(list(root.outOrder), [7, 6, 5, 4, 3, 2, 1])

        self.assertEqual(list(root.postOrder), [1, 3, 2, 5, 7, 6, 4])

        self.assertEqual(list(root), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(list(reversed(root)), [7, 6, 5, 4, 3, 2, 1])


    def test_binaryTree_equality(self):
        node1 = self.Node(1)
        node3 = self.Node(3)
        node5 = self.Node(5)
        node7 = self.Node(7)

        node2 = self.Node(2, node1, node3)
        node6 = self.Node(6, node5, node7)

        node4 = self.Node(4, node2, node6)

        rootA = node4
        rootB = node6
        rootC = node2

        self.assertTrue(rootA == rootA)
        self.assertFalse(rootA == rootB)
        self.assertFalse(rootA == rootC)

        self.assertFalse(rootB == rootA)
        self.assertTrue(rootB == rootB)
        self.assertFalse(rootB == rootC)

        self.assertFalse(rootC == rootA)
        self.assertFalse(rootC == rootB)
        self.assertTrue(rootC == rootC)

if __name__ == '__main__':
    unittest.main()