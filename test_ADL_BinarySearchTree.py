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



if __name__ == '__main__':
    unittest.main()