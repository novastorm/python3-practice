import binaryTree

from binaryTree import TreeNode

class BinaryTree(binaryTree.BinaryTree):
    def max_sum_path(self, root):
        memo = [0]

        def helper(node, memo=memo):
            if not node:
                return 0

            leftSum = helper(node.left_child) if node.left_child else 0
            rightSum = helper(node.right_child) if node.right_child else 0

            max_cummulative_sum = max(
                node.data + leftSum,
                node.data + rightSum
            )

            memo[0] = max(
                memo[0],
                leftSum + node.data + rightSum
            )

            return max_cummulative_sum

        helper(root)

        return memo[0]


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


if __name__ == '__main__':
        unittest.main()
