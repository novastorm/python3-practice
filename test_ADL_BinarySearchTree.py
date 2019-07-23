import unittest
from ADL_BinarySearchTree import *

class Base_ADL_BinaryTree_tests(unittest.TestCase):

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
        print(str(self.aBST))

        self.aBST.insertValue(2)
        self.assertEqual(len(self.aBST), 2)
        print(str(self.aBST))

        self.aBST.insertValue(1)
        self.assertEqual(len(self.aBST), 3)
        print(str(self.aBST))

        self.aBST.insertValue(3)
        self.assertEqual(len(self.aBST), 4)
        print(str(self.aBST))

        self.aBST.insertValue(6)
        self.assertEqual(len(self.aBST), 5)
        print(str(self.aBST))

        self.aBST.insertValue(5)
        self.assertEqual(len(self.aBST), 6)
        print(str(self.aBST))

        self.aBST.insertValue(7)
        self.assertEqual(len(self.aBST), 7)
        print(str(self.aBST))

        for e in self.aBST:
            print(e)

        for e in self.aBST.inOrder:
            print(e)

        for e in self.aBST.preOrder:
            print(e)

if __name__ == '__main__':
    unittest.main()