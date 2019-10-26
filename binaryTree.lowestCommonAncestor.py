import binaryTree

from binaryTree import TreeNode

class BinaryTree(binaryTree.BinaryTree):

    @staticmethod
    def get_path(root, target):
        queue = []
        queue.append((root, [root]))

        while queue:
            next, path = queue.pop(0)
            if next == target:
                return path
            if next.left_child:
                queue.append((next.left_child, path + [next.left_child]))
            if next.right_child:
                queue.append((next.right_child, path + [next.right_child]))
        return []

    @staticmethod
    def lowest_common_ancestor_1(root, a, b):
        get_path = BinaryTree.get_path

        pathA = get_path(root, a)
        pathB = get_path(root, b)

        node = None

        for nodeA, nodeB in zip(pathA, pathB):
            if nodeA == nodeB:
                node = nodeA

        return node

    @staticmethod
    def lowest_common_ancestor_recursive(root, node_a, node_b):
        lowest_common_ancestor_recursive = BinaryTree.lowest_common_ancestor_recursive

        if not root or not node_a or not node_b:
            return None

        left = None
        right = None

        if root == node_a or root == node_b:
            return root

        left = lowest_common_ancestor_recursive(root.left_child, node_a, node_b)
        right = lowest_common_ancestor_recursive(root.right_child, node_a, node_b)

        if left and right:
            return root  

        return if left else right


###############################################################################

import unittest


class Test_BinaryTree_lowest_common_ancestor(unittest.TestCase):

    def test_lowest_common_ancestor_1(self):
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

        a = nodes[6]
        b = nodes[4]
        e = nodes[1]
        self.assertEqual(BinaryTree().lowest_common_ancestor_1(root, a, b), e)

        a = nodes[4]
        b = nodes[5]
        e = nodes[2]
        self.assertEqual(BinaryTree().lowest_common_ancestor_1(root, a, b), e)


    def test_lowest_common_ancestor_recursive(self):
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

        a = nodes[6]
        b = nodes[4]
        e = nodes[1]
        self.assertEqual(BinaryTree().lowest_common_ancestor_recursive(root, a, b), e)

        a = nodes[4]
        b = nodes[5]
        e = nodes[2]
        self.assertEqual(BinaryTree().lowest_common_ancestor_recursive(root, a, b), e)


if __name__ == '__main__':
        unittest.main()
