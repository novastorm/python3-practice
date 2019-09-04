class BinaryTreeError(Exception):
    """Base (catch-all) binarytree exception."""
    pass


class NodeTypeError(BinaryTreeError):
    """Node was not an instance of :class:`binarytree.Node`."""
    pass


class NodeValueError(BinaryTreeError):
    """Node value was not a valid."""
    pass


class ADL_BinaryTree:

    def isEqualToOther(self, other):
        if not isinstance(other, ADL_BinaryTree):
            raise NotImplementedError

        for leftList, rightList in zip(self.breadthFirst, other.breadthFirst):
            if leftList != rightList:
                return False

        return True

    def __eq__(self, other):
        return self.isEqualToOther(other)

    def __len__(self):
        raise NotImplementedError

    def __str__(self):
        s = "["
        sep = ""
        for i in self:
            s += sep + str(i)
            sep = ", "
        s += "]"
        return s

    def breadthFirst(self):
        raise NotImplementedError

    def preOrder(self):
        raise NotImplementedError

    def inOrder(self):
        raise NotImplementedError

    def outOrder(self):
        raise NotImplementedError

    def postOrder(self):
        raise NotImplementedError

    def __iter__(self):
        return self.inOrder

    def __reversed__(self):
        return self.outOrder


class ADL_BinaryTreeNode:

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


class ADL_BinaryTreeNode_Iterative(ADL_BinaryTreeNode, ADL_BinaryTree):
    '''BinaryTree Implementation'''

    def __init__(self, value, left=None, right=None):

        if left is not None and not isinstance(left, ADL_BinaryTree):
            raise NodeTypeError('left child must be a ADL_BinaryTree instance')
        if right is not None and not isinstance(right, ADL_BinaryTree):
            raise NodeTypeError('right child must be a ADL_BinaryTree instance')

        self.value = value
        self.left = left
        self.right = right


    class BreadthFirstIterator:
        def __init__(self, node):
            """Initialize the iterator"""
            self.queue = []
            self.queue.append(node)

        def __iter__(self):
            return self

        def  __next__(self):
            """Return the next value"""
            if len(self.queue) == 0:
                raise StopIteration

            nextNode = self.queue.pop(0)

            if nextNode.left:
                self.queue.append(nextNode.left)
            if nextNode.right:
                self.queue.append(nextNode.right)

            return nextNode.value

    @property
    def breadthFirst(self):
        return self.BreadthFirstIterator(self)


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
                currNode = currNode.left

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
                currNode = currNode.right

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

        def insertNodes(self, node):
            currNode = node
            while currNode:
                if currNode.right :  # is not None:
                    self.stack.append(currNode.right)

                self.stack.append(currNode)

                currNode = currNode.left


        def __init__(self, node):
            self.stack = []

            self.insertNodes(node)

        def __iter__(self):
            return self

        def __next__(self):
            if not self.stack:
                raise StopIteration

            nextNode = self.stack.pop()

            currNode = nextNode
            if currNode.right and self.stack and currNode.right == self.stack[-1]:
                result = self.stack.pop()

                self.stack.append(currNode)
                
                self.insertNodes(currNode.right)

                nextNode = self.stack.pop()

            return nextNode.value


    @property
    def postOrder(self):
        return self.PostOrderIterator(self)

    def __iter__(self):
        return self.inOrder

    def __reversed__(self):
        return self.outOrder
