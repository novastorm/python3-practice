from abc import ABCMeta, abstractmethod

class BinaryTreeError(Exception):
    """Base (catch-all) binarytree exception."""
class NodeTypeError(BinaryTreeError):
    """Node was not an instance of :class:`binarytree.Node`."""
class NodeValueError(BinaryTreeError):
    """Node value was not a valid."""


class ADL_BinaryTree:
    '''BinaryTree Implementation'''

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

    
    @property
    def __len__(self):
        return (self.left.__len__() if self.left else 0) + 1 + (self.right.__len__() if self.right else 0)


    def __init__(self, value, left=None, right=None):

        if left is not None and not isinstance(left, ADL_BinaryTree):
            raise NodeTypeError('left child must be a ADL_BinaryTree instance')
        if right is not None and not isinstance(right, ADL_BinaryTree):
            raise NodeTypeError('right child must be a ADL_BinaryTree instance')

        self.value = value
        self.left = left
        self.right = right