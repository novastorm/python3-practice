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

    class PreOrderIterator:
        def __init__(self, node):
            self.stack = []
            self.stack.append(node)

        def __iter__(self):
            return self

        def __next__(self):
            if len(self.stack) == 0:
                raise StopIteration

            nextNode = self.stack.pop()

            if nextNode.right is not None:
                self.stack.append(nextNode.right)
            if nextNode.left is not None:
                self.stack.append(nextNode.left)

            return nextNode.value

    @property
    def preOrder(self):
        return self.PreOrderIterator(self._root)

    class InOrderIterator:
        def __init__(self, node):
            self.stack = []
            currNode = node
            while currNode is not None:
                self.stack.append(currNode)
                currNode = currNode._left

        def __iter__(self):
            return self

        def __next__(self):
            if len(self.stack) == 0:
                raise StopIteration
            nextNode = self.stack.pop()
            currNode = nextNode.right

            while currNode is not None:
                self.stack.append(currNode)
                currNode = currNode.left

            return nextNode.value

    @property
    def inOrder(self):
        return self.InOrderIterator(self._root)

    class OutOrderIterator:
        def __init__(self, node):
            self.stack = []
            currNode = node
            while currNode is not None:
                self.stack.append(currNode)
                currNode = currNode._right

        def __iter__(self):
            return self

        def __next__(self):
            if len(self.stack) == 0:
                raise StopIteration
            nextNode = self.stack.pop()
            currNode = nextNode.left

            while currNode is not None:
                self.stack.append(currNode)
                currNode = currNode.right

            return nextNode.value

    @property
    def outOrder(self):
        return self.OutOrderIterator(self._root)    

    def __iter__(self):
        return self.inOrder

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
