from collections import deque


class NTreeError(Exception):
    """Base (catch-all) binarytree exception."""
    pass


class NTreeNodeTypeError(NTreeError):
    """Node was not an instance of :class:`binarytree.Node`."""
    pass


class NTreeNodeValueError(NTreeError):
    """Node value was not a valid."""
    pass


class ADL_NTreeNode:

    def __init__(self, value):
        self._value = value
        self._children = []

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

    # def __len__(self):
    #     return 1 + (sum([len(c) for c in self.children]) if self.children else 0)


class ADL_NTree:

    def isEqualToOther(self, other):
        if not isinstance(other, ADL_NTree):
            False

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
                   raise NTreeNodeTypeError('all children nodes   must be a ADL_NTree instance')

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


    class PreOrderIterator:
        def __init__(self, node):
            self.stack = []
            self.stack.append(node)

        def __iter__(self):
            return self

        def __next__(self):
            if not self.stack:
                raise StopIteration

            next = self.stack.pop()

            for n in next.children[::-1]:
                self.stack.append(n)

            return next.value

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


###############################################################################

import unittest


class Test_NTree(unittest.TestCase):

    def test_1(self):

        nodes = {}

        for i in range(16):
            nodes[i] = ADL_NTreeNode(i)

        root = nodes[0]
        nodes[0].children = [nodes[1], nodes[2], nodes[3]]
        nodes[1].children = [nodes[4], nodes[5], nodes[6]]
        nodes[2].children = [nodes[7], nodes[8], nodes[9]]
        nodes[3].children = [nodes[10], nodes[11], nodes[12]]
        nodes[4].children = [nodes[13], nodes[14], nodes[15]]

        aBFS = ADL_NTreeNode_Iterative.BreadthFirstIterator(root)
        print(list(aBFS))
        aPreDFS = ADL_NTreeNode_Iterative.PreOrderIterator(root)
        print(list(aPreDFS))
        aPostDFS = ADL_NTreeNode_Iterative.PostOrderIterator(root)
        print(list(aPostDFS))

        i = None
        e = None
        self.assertEqual(i, e)

if __name__ == '__main__':
    unittest.main()
