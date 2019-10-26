class TreeNode:
    def __init__(self, data,left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return '%s' %self.data


class BinaryTree:

    def __init__(self, root_node = None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node

    # Helper method
    def find_min(self,root):
        if root == None:
            return None
        if root.left_child == None:
            return root
        return self.find_min(root.left_child)

    def delete(self, root, data):
        # Return the new root node of type TreeNode
        if not root:
            return root

        if data < root.data:
            root.left_child = self.delete(root.left_child, data)
        elif root.data < data:
            root.right_child = self.delete(root.right_child, data)
        else:
            if root.left_child and root.right_child:
                root.data = self.find_min(root.right_child).data
                root.right_child = self.delete(root.right_child, root.data)
            elif not root.left_child and not root.right_child:
                if root is self.root:
                    self.root = None
                root = None
            elif not root.right_child:
                    if root is self.root:
                        self.root = root.left_child
                    root = root.left_child
            else:
                if root is self.root:
                    self.root = root.right_child
                root = root.right_child

        return root


###############################################################################

import unittest


class Test_BinaryTree_max_sum_path(unittest.TestCase):

    class BreadthFirstIterator:
        def __init__(self, node):
            self.queue = [node]

        def __iter__(self):
            return self

        def __next__(self):
            if len(self.queue) == 0:
                raise StopIteration

            nextNode = self.queue.pop(0)

            if nextNode:
                self.queue.append(nextNode.left_child)
                self.queue.append(nextNode.right_child)

            return nextNode.data if nextNode else None

        next = __next__

    def test_0(self):
        nodes = {}
        for i in [4, 2, 8, 5, 10]:
            nodes[i] = TreeNode(i)

        root = nodes[4]
        nodes[4].left_child = nodes[2]
        nodes[4].right_child = nodes[8]
        nodes[8].left_child = nodes[5]
        nodes[8].right_child = nodes[10]

        tree = BinaryTree(root).delete(root, 10)
        self.assertEqual(list(self.BreadthFirstIterator(tree)), [
            4,
            2, 8,
            None, None, 5, None,
            None, None])


    def test_1(self):
        nodes = {}
        for i in [6,4,8,1,5,7,9]:
            nodes[i] = TreeNode(i)

        root = nodes[6]
        nodes[6].left_child = nodes[4]
        nodes[6].right_child = nodes[8]
        nodes[4].left_child = nodes[1]
        nodes[4].right_child = nodes[5]
        nodes[8].left_child = nodes[7]
        nodes[8].right_child = nodes[9]

        tree = BinaryTree(root).delete(root, 4)
        self.assertEqual(list(self.BreadthFirstIterator(tree)), [
            6,
            5, 8,
            1, None, 7, 9,
            None, None, None, None, None, None,
        ])

    def test_2(self):
        nodes = {}
        for i in [1]:
            nodes[i] = TreeNode(i)

        root = nodes[1]

        tree = BinaryTree(root).delete(root, 1)
        self.assertEqual(list(self.BreadthFirstIterator(tree)), [None])

    def test_3(self):

        root = None

        tree = BinaryTree(root).delete(root, 1)
        self.assertEqual(list(self.BreadthFirstIterator(tree)), [None])

    def test_4(self):
        nodes = {}
        for i in [9, 3, 2, 4, 1, 5]:
            nodes[i] = TreeNode(i)

        root = nodes[9]
        nodes[9].left_child = nodes[3]
        nodes[3].left_child = nodes[2]
        nodes[3].right_child = nodes[4]
        nodes[2].left_child = nodes[1]
        nodes[4].right_child = nodes[5]

        tree = BinaryTree(root).delete(root, 3)
        self.assertEqual(list(self.BreadthFirstIterator(tree)), [
            9,
            4, None,
            2, 5,
            1, None, None, None,
            None, None
        ])

    def test_5(self):
        nodes = {}
        for i in [9, 4, 2, 8, 1, 5]:
            nodes[i] = TreeNode(i)

        root = nodes[9]
        nodes[9].left_child = nodes[4]
        nodes[4].left_child = nodes[2]
        nodes[4].right_child = nodes[8]
        nodes[2].left_child = nodes[1]
        nodes[8].left_child = nodes[5]

        tree = BinaryTree(root).delete(root, 9)
        self.assertEqual(list(self.BreadthFirstIterator(tree)), [
            4,
            2, 8,
            1, None, 5, None,
            None, None, None, None
        ])

    def test_6(self):
        nodes = {}
        for i in [6, 4, 7, 1, 5, 9]:
            nodes[i] = TreeNode(i)

        root = nodes[6]
        nodes[6].left_child = nodes[4]
        nodes[6].right_child = nodes[7]
        nodes[4].left_child = nodes[1]
        nodes[4].right_child = nodes[5]
        nodes[7].right_child = nodes[9]

        tree = BinaryTree(root).delete(root, 7)
        self.assertEqual(list(self.BreadthFirstIterator(tree)), [
            6,
            4, 9,
            1, 5, None, None,
            None, None, None, None
        ])

if __name__ == '__main__':
        unittest.main()
