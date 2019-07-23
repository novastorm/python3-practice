from ADL_BinaryTree import *

class ADL_BinarySearchTree:

    @property
    def isEmpty(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError


    def insertValue(self, value):
        raise NotImplementedError


    def findValue(self):
        raise NotImplementedError


    def removeValue(self):
        raise NotImplementedError


    def inorderTraversal(self, callback):
        raise NotImplementedError


    def outOrderTraversal(self, callback):
        raise NotImplementedError


    @staticmethod
    def isBinarySearchTree(tree):
        raise NotImplementedError


class ADL_BinarySearchTree_graph(ADL_BinarySearchTree):

    def __init__(self):
        self._root = None

    def __len__(self):
        return len(self._root) if self._root else 0

    @property
    def preOrder(self):
        return self._root.preOrder if self._root else []

    @property
    def inOrder(self):
        return self._root.inOrder if self._root else []

    @property
    def outOrder(self):
        return self._root.outOrder if self._root else []


    @property
    def postOrder(self):
        return self._root.postOrder if self._root else []

    def __iter__(self):
        return self.inOrder

    def __reversed__(self):
        return self.outOrder

    def __str__(self):
        s = "["
        sep = ""
        for i in self:
            s += sep + str(i)
            sep = ", "
        s += "]"
        return s

    def insertValue(self, value):
        node = ADL_BinaryTree(value)

        if self._root is None:
            self._root = node
            return

        self._insertNode(self._root, node)

    def _insertNode(self, root, node):
        if root is None:
            return

        if root.value < node.value:
            if root.right is None:
                root.right = node
            else:
                self._insertNode(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                self._insertNode(root.left, node)
        

class ADL_BinarySearchTree_list(ADL_BinarySearchTree):
    pass
