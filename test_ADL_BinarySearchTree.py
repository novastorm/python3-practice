import unittest
from ADL_BinarySearchTree import *

class Base_ADL_BinarySearchTree_tests(unittest.TestCase):

    def setUp(self):
        self.aBST = ADL_BinarySearchTree_graph()


    def tearDown(self):
        self.aBST = None


    def test_binarySearchTree_initialize(self):
        self.assertTrue(isinstance(self.aBST, ADL_BinarySearchTree))
        self.assertEqual(len(self.aBST), 0)
        self.assertEqual(list(self.aBST), [])


    def test_binarySearchTree_insert(self):
        self.aBST.insertValue(4)
        self.assertEqual(len(self.aBST), 1)
        self.assertEqual(list(self.aBST.inOrder), [4])

        self.aBST.insertValue(2)
        self.assertEqual(len(self.aBST), 2)
        self.assertEqual(list(self.aBST.inOrder), [2, 4])

        self.aBST.insertValue(1)
        self.assertEqual(len(self.aBST), 3)
        self.assertEqual(list(self.aBST.inOrder), [1, 2, 4])

        self.aBST.insertValue(3)
        self.assertEqual(len(self.aBST), 4)
        self.assertEqual(list(self.aBST.inOrder), [1, 2, 3, 4])

        self.aBST.insertValue(6)
        self.assertEqual(len(self.aBST), 5)
        self.assertEqual(list(self.aBST.inOrder), [1, 2, 3, 4, 6])

        self.aBST.insertValue(5)
        self.assertEqual(len(self.aBST), 6)
        self.assertEqual(list(self.aBST.inOrder), [1, 2, 3, 4, 5, 6])

        self.aBST.insertValue(7)
        self.assertEqual(len(self.aBST), 7)

        self.assertEqual(list(self.aBST.breadthFirst), [4, 2, 6, 1, 3, 5, 7])

        self.assertEqual(list(self.aBST.preOrder), [4, 2, 1, 3, 6, 5, 7])

        self.assertEqual(list(self.aBST.inOrder), [1, 2, 3, 4, 5, 6, 7])

        self.assertEqual(list(self.aBST.outOrder), [7, 6, 5, 4, 3, 2, 1])

        self.assertEqual(list(self.aBST.postOrder), [1, 3, 2, 5, 7, 6, 4])

        self.assertEqual(list(self.aBST), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(list(reversed(self.aBST)), [7, 6, 5, 4, 3, 2, 1])


    def test_binarySearchTree_equality(self):
        Node = ADL_BinaryTreeNode_Iterative
        BST = ADL_BinarySearchTree_graph
        
        aBST = BST()
        aBST.insertValue(4)
        aBST.insertValue(2)
        aBST.insertValue(1)
        aBST.insertValue(3)
        aBST.insertValue(6)
        aBST.insertValue(5)
        aBST.insertValue(7)


        node1 = Node(1)
        node3 = Node(3)
        node5 = Node(5)
        node7 = Node(7)

        node2 = Node(2, node1, node3)
        node6 = Node(6, node5, node7)

        node4 = Node(4, node2, node6)

        rootA = node4
        rootB = node6
        rootC = node2

        self.assertTrue(rootA == aBST)
        self.assertFalse(rootB == aBST)
        self.assertFalse(rootC == aBST)
        self.assertTrue(aBST == rootA)
        self.assertFalse(aBST == rootB)
        self.assertFalse(aBST == rootC)


    def test_BSTGraph_findNodeRecursive(self):
        aBST = ADL_BinarySearchTree_graph()

        aBST.insertValue(4)
        aBST.insertValue(2)
        aBST.insertValue(1)
        aBST.insertValue(3)
        aBST.insertValue(6)
        aBST.insertValue(5)
        aBST.insertValue(7)

        self.assertTrue(aBST._findNodeRecursive(aBST._root, 4))
        self.assertTrue(aBST._findNodeRecursive(aBST._root, 1))
        self.assertTrue(aBST._findNodeRecursive(aBST._root, 3))
        self.assertTrue(aBST._findNodeRecursive(aBST._root, 5))
        self.assertTrue(aBST._findNodeRecursive(aBST._root, 6))
        self.assertTrue(aBST._findNodeRecursive(aBST._root, 7))

        self.assertFalse(aBST._findNodeRecursive(aBST._root, 0))
        self.assertFalse(aBST._findNodeRecursive(aBST._root, 8))


    def test_BSTGraph_findNodeIterative(self):
        aBST = ADL_BinarySearchTree_graph()

        aBST.insertValue(4)
        aBST.insertValue(2)
        aBST.insertValue(1)
        aBST.insertValue(3)
        aBST.insertValue(6)
        aBST.insertValue(5)
        aBST.insertValue(7)

        self.assertTrue(aBST._findNodeIterative(aBST._root, 4))
        self.assertTrue(aBST._findNodeIterative(aBST._root, 1))
        self.assertTrue(aBST._findNodeIterative(aBST._root, 3))
        self.assertTrue(aBST._findNodeIterative(aBST._root, 5))
        self.assertTrue(aBST._findNodeIterative(aBST._root, 6))
        self.assertTrue(aBST._findNodeIterative(aBST._root, 7))

        self.assertFalse(aBST._findNodeIterative(aBST._root, 0))
        self.assertFalse(aBST._findNodeIterative(aBST._root, 8))


    def test_BSTGraph_find(self):
        aBST = ADL_BinarySearchTree_graph()

        aBST.insertValue(4)
        aBST.insertValue(2)
        aBST.insertValue(1)
        aBST.insertValue(3)
        aBST.insertValue(6)
        aBST.insertValue(5)
        aBST.insertValue(7)

        self.assertTrue(aBST.findValue(4))
        self.assertTrue(aBST.findValue(1))
        self.assertTrue(aBST.findValue(3))
        self.assertTrue(aBST.findValue(5))
        self.assertTrue(aBST.findValue(6))
        self.assertTrue(aBST.findValue(7))

        self.assertFalse(aBST.findValue(0))
        self.assertFalse(aBST.findValue(8))


    def test_BSTGraph_empty_remove(self):
        aBST = ADL_BinarySearchTree_graph()

        with self.assertRaises(ValueError):
            aBST.removeValue(0)


    def test_BSTGraph_one_value_remove(self):
        # print()
        aBST = ADL_BinarySearchTree_graph()

        aBST.insertValue(8)
        # print(aBST)

        aBST.removeValue(8)
        # print(aBST)


    def test_BSTGraph_remove_root(self):
        # print()
        aBST = ADL_BinarySearchTree_graph()

        aBST.insertValue(8)
        aBST.insertValue(4)
        aBST.insertValue(12)
        aBST.insertValue(10)
        aBST.insertValue(11)
        aBST.insertValue(14)

        # print(aBST)

        aBST.removeValue(8)

        # print(aBST)


    def test_BSTGraph_remove_subnode_1(self):
        # print()
        aBST = ADL_BinarySearchTree_graph()

        aBST.insertValue(8)
        aBST.insertValue(4)
        aBST.insertValue(12)
        aBST.insertValue(14)
        aBST.insertValue(13)
        aBST.insertValue(15)

        # print(aBST)

        aBST.removeValue(12)

        # print(aBST)


    def test_BSTGraph_remove_subnode_2(self):
        # print()
        aBST = ADL_BinarySearchTree_graph()

        aBST.insertValue(8)
        aBST.insertValue(4)
        aBST.insertValue(12)
        aBST.insertValue(10)
        aBST.insertValue(11)
        aBST.insertValue(14)
        aBST.insertValue(15)

        # print(aBST)

        aBST.removeValue(12)

        # print(aBST)


if __name__ == '__main__':
    unittest.main()