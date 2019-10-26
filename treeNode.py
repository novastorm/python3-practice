class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


###############################################################################

import unittest


class Test_TreeNode(unittest.TestCase):

    def test_initialize(self):
        node = TreeNode(0)

        e = 0
        self.assertEqual(node.data, e)
        self.assertIsNone(node.left_child)
        self.assertIsNone(node.right_child)

    def test_tree(self):
        nodes = {}
        for i in range(3):
            nodes[i] = TreeNode(i)

        root = nodes[0]
        nodes[0].left_child = nodes[1]
        nodes[0].right_child = nodes[2]

        self.assertEqual(root.data, 0)
        self.assertEqual(root.left_child.data, 1)
        self.assertEqual(root.right_child.data, 2)

        
if __name__ == '__main__':
        unittest.main()
