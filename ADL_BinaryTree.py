from abc import ABCMeta, abstractmethod



class ADL_BinaryTree:
    '''BinaryTree Implementation'''

    class BinaryTreeError(Exception):
        """Base (catch-all) binarytree exception."""
    class NodeTypeError(BinaryTreeError):
        """Node was not an instance of :class:`binarytree.Node`."""
    class NodeValueError(BinaryTreeError):
        """Node value was not a valid."""

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, newValue):
        self._value = newValue


    @property
    def left(self):
        return self._left
    @left.setter
    def left(self, newValue):
        if newValue is not None and not isinstance(newValue, ADL_BinaryTree):
            raise NodeTypeError('left child must be a ADL_BinaryTree instance')
        self._left = newValue

    @property
    def right(self):
        return self._right
    @right.setter
    def right(self, newValue):
        if newValue is not None and not isinstance(newValue, ADL_BinaryTree):
            raise NodeTypeError('right child must be a ADL_BinaryTree instance')
        self._right = newValue

    
    def __len__(self):
        return (len(self.left) if self.left else 0) + 1 + (len(self.right) if self.right else 0)


    def __init__(self, value, left=None, right=None):

        if left is not None and not isinstance(left, ADL_BinaryTree):
            raise NodeTypeError('left child must be a ADL_BinaryTree instance')
        if right is not None and not isinstance(right, ADL_BinaryTree):
            raise NodeTypeError('right child must be a ADL_BinaryTree instance')

        self.value = value
        self.left = left
        self.right = right


    def __str__(self):
        return self._value

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

            if nextNode.right: # is not None:
                self.stack.append(nextNode.right)
            if nextNode.left: # is not None:
                self.stack.append(nextNode.left)

            return nextNode.value

    @property
    def preOrder(self):
        return self.PreOrderIterator(self)

    class InOrderIterator:
        def __init__(self, node):
            self.stack = []
            currNode = node
            while currNode: # is not None:
                self.stack.append(currNode)
                currNode = currNode._left

        def __iter__(self):
            return self

        def __next__(self):
            if len(self.stack) == 0:
                raise StopIteration

            nextNode = self.stack.pop()
            currNode = nextNode.right

            while currNode: # is not None:
                self.stack.append(currNode)
                currNode = currNode.left

            return nextNode.value

    @property
    def inOrder(self):
        return self.InOrderIterator(self)

    class OutOrderIterator:
        def __init__(self, node):
            self.stack = []
            currNode = node
            while currNode: # is not None:
                self.stack.append(currNode)
                currNode = currNode._right

        def __iter__(self):
            return self

        def __next__(self):
            if len(self.stack) == 0:
                raise StopIteration

            nextNode = self.stack.pop()
            currNode = nextNode.left

            while currNode: # is not None:
                self.stack.append(currNode)
                currNode = currNode.right

            return nextNode.value

    @property
    def outOrder(self):
        return self.OutOrderIterator(self)    

    class PostOrderIterator:
        def __init__(self, node):
            self.stack = []
            currNode = node
            while currNode: # is not None:
                if currNode.right: # is not None:
                    self.stack.append(currNode.right)
                self.stack.append(currNode)
                currNode = currNode.left

        def __iter__(self):
            return self

        def __next__(self):
            if not self.stack: # is stack is empty
                raise StopIteration

            nextNode = self.stack.pop()

            currNode = nextNode
            if currNode.right and self.stack and currNode.right == self.stack[-1]:
                self.stack.pop()
                self.stack.append(currNode)
                currNode = currNode.right
                while currNode: # is not None:
                    if currNode.right: # is not None:
                        self.stack.append(currNode.right)
                    self.stack.append(currNode)
                    currNode = currNode.left
                nextNode = self.stack.pop()

            return nextNode.value


    @property
    def postOrder(self):
        return self.PostOrderIterator(self)