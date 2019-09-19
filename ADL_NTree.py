from collections import deque


class NTreeError(Exception):
    """Base (catch-all) binarytree exception."""
    pass


class NodeTypeError(NTreeError):
    """Node was not an instance of :class:`binarytree.Node`."""
    pass


class NodeValueError(NTreeError):
    """Node value was not a valid."""
    pass


class ADL_NTreeNode:

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newValue):
        self._value = newValue

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, newValue):
        self._children = newValue

    def __len__(self):
        return 1 + (sum([len(c) for c in self.children]) if self.children else 0)


class ADL_NTree:

    def isEqualToOther(self, other):
        if not isinstance(other, ADL_NTree):
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

    def graphRepresentation(self):
        raise NotImplementedError


class ADL_NTreeNode_Iterative(ADL_NTreeNode, ADL_NTree):
    '''BinaryTree Implementation'''

    def __init__(self, value, children=[]):

        if children:
            for node in children:
                if node is not None and not isinstance(node, ADL_NTree):
                   raise NodeTypeError('all children nodes   must be a ADL_NTree instance')

        self._value = value
        self._children = children

    class BreadthFirstIterator:
        def __init__(self, node):
            self.queue = deque()
            if node:
                self.queue.append(node)

        def __iter__(self):
            return self

        def __next__(self):
            if not self.queue:
                raise StopIteration

            nextNode = self.queue.popleft()

            if nextNode.children:
                self.queue.extend(nextNode.children)

            return nextNode.value

    @property
    def breadthFirst(self):
        return self.BreadthFirstIterator(self)


    class PostOrderIterator:

        def insertNodes(self, node):
            currNode = node
            while currNode:
                if not currNode.children:
                    currNode = None
                else:
                    for n in currNode.children[::-1]:
                        self.stack.extend([n, n])
                    currNode = self.stack.pop()


        def __init__(self, node):
            self.stack = []

            if not node:
                return

            self.stack.append(node)
            self.insertNodes(node)

        def __iter__(self):
            return self

        def __next__(self):
            if not self.stack:
                raise StopIteration

            currNode = self.stack.pop()

            if self.stack and currNode is self.stack[-1]:
                self.insertNodes(self.stack[-1])
                currNode = self.stack.pop()

            return currNode.value

    @property
    def postOrder(self):
        return self.PostOrderIterator(self)

