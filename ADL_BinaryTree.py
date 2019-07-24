from abc import ABCMeta, abstractmethod

class BinaryTreeError(Exception):
    """Base (catch-all) binarytree exception."""
class NodeTypeError(BinaryTreeError):
    """Node was not an instance of :class:`binarytree.Node`."""
class NodeValueError(BinaryTreeError):
    """Node value was not a valid."""    

class ADL_BinaryTree:

    def isEqualToOther(self, other):
        if not isinstance(other, ADL_BinaryTree):
            raise NotImplementedError

        for l,r in zip(self.breadthFirst, other.breadthFirst):
            if l != r:
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
            # dequeue the next node
            nextNode = self.queue.pop(0)
            # enqueue node's chilren to the queue
            if nextNode.left:
                self.queue.append(nextNode.left)
            if nextNode.right:
                self.queue.append(nextNode.right)
            # return nextNode's value
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
            # print(list(map(lambda x: x.value, self.stack)))
            currNode = node
            while currNode: # is not None:
                if currNode.right: # is not None:
                    self.stack.append(currNode.right)
                    # print("push", currNode.right.value, list(map(lambda x: x.value, self.stack)))
                self.stack.append(currNode)
                # print("push", currNode.value, list(map(lambda x: x.value, self.stack)))
                currNode = currNode.left

        def __iter__(self):
            return self

        def __next__(self):
            # print(list(map(lambda x: x.value, self.stack)))
            if not self.stack: # is stack is empty
                raise StopIteration

            nextNode = self.stack.pop()
            # print("pop", nextNode.value, list(map(lambda x: x.value, self.stack)))

            currNode = nextNode
            if currNode.right and self.stack and currNode.right == self.stack[-1]:
                result = self.stack.pop()
                # print("pop", result.value, list(map(lambda x: x.value, self.stack)))
                self.stack.append(currNode)
                # print("push", currNode.value, list(map(lambda x: x.value, self.stack)))
                currNode = currNode.right
                while currNode: # is not None:
                    if currNode.right: # is not None:
                        self.stack.append(currNode.right)
                        # print("push", currNode.right.value, list(map(lambda x: x.value, self.stack)))
                    self.stack.append(currNode)
                    # print("push", currNode.value, list(map(lambda x: x.value, self.stack)))
                    currNode = currNode.left
                nextNode = self.stack.pop()
                # print("pop", nextNode.value, list(map(lambda x: x.value, self.stack)))


            # print(">>", nextNode.value)
            return nextNode.value


    @property
    def postOrder(self):
        return self.PostOrderIterator(self)

    def __iter__(self):
        return self.inOrder

    def __reversed__(self):
        return self.outOrder

        
'''
[]
push 6 [6]
push 4 [6, 4]
push 3 [6, 4, 3]
push 2 [6, 4, 3, 2]
push 1 [6, 4, 3, 2, 1]
[6, 4, 3, 2, 1]
pop 1 [6, 4, 3, 2]
>> 1
[6, 4, 3, 2]
pop 2 [6, 4, 3]
pop 3 [6, 4]
push 2 [6, 4, 2]
push 3 [6, 4, 2, 3]
pop 3 [6, 4, 2]
>> 3
[6, 4, 2]
pop 2 [6, 4]
>> 2
[6, 4]
pop 4 [6]
pop 6 []
push 4 [4]
push 7 [4, 7]
push 6 [4, 7, 6]
push 5 [4, 7, 6, 5]
pop 5 [4, 7, 6]
>> 5
[4, 7, 6]
pop 6 [4, 7]
pop 7 [4]
push 6 [4, 6]
push 7 [4, 6, 7]
pop 7 [4, 6]
>> 7
[4, 6]
pop 6 [4]
>> 6
[4]
pop 4 []
>> 4
[]
'''
