from treeNode import TreeNode

class BinaryTree:
    def __init__(self, root_node=None):
            self.root = root_node


###############################################################################

import unittest


class Test_BinaryTree_max_sum_path(unittest.TestCase):

    def setUp(self):
        nodes = {}
        for i in range(8):
            nodes[i] = TreeNode(i)

        self.root = nodes[1]
        nodes[1].left_child = nodes[2]
        nodes[1].right_child = nodes[3]
        nodes[2].left_child = nodes[4]
        nodes[2].right_child = nodes[5]
        nodes[3].left_child = nodes[6]
        nodes[3].right_child = nodes[7]

    def test_max_cummulative_sum(self):
        self.assertEqual(BinaryTree().max_sum_path(self.root), 18)

class Test_BinaryTree_lowest_common_ancestor(unittest.TestCase):

    def test_lowest_common_ancestor(self):
        nodes = {}
        for i in range(1, 8):
            nodes[i] = TreeNode(i)

        root = nodes[1]
        nodes[1].left_child = nodes[2]
        nodes[1].right_child = nodes[3]
        nodes[2].left_child = nodes[4]
        nodes[2].right_child = nodes[5]
        nodes[3].left_child = nodes[6]
        nodes[3].right_child = nodes[7]

        a = 6
        b = 4
        e = 1
        self.assertEqual(BinaryTree().lowest_common_ancestor(root, a, b).data, e)

        a = 4
        b = 5
        e = 2
        self.assertEqual(BinaryTree().lowest_common_ancestor(root, a, b).data, e)

        
if __name__ == '__main__':
        unittest.main()
