from os import abort
from ADL_SinglyLinkedListNode import *

class ADL_SinglyLinkedList:
    """Singly Linked List Implementation"""

    def __init__(self):
        self._head = None
        self._last = None


    def __len__(self):
        """Return the number of nodes from this node"""
        if self._head is None:
            return 0

        return len(self._head)


    def __str__(self):
        """Return the string description of this list"""
        s = "["
        sep = ""
        for i in self._head:
            s += sep + str(i)
            sep = ", "
        s += "]"
        return s


    def __getitem__(self, index):
        assert 0 <= index and index < len(self), "index out of bounds"

        nodeAtIndex = self._head
        for i in range(index):
            nodeAtIndex = nodeAtIndex.next

        return nodeAtIndex.value

    def __setitem__(self, index, value):
        assert 0 <= index and index < len(self), "index out of bounds"

        nodeAtIndex = self._head
        for i in range(index):
            nodeAtIndex = nodeAtIndex.next

        oldValue = nodeAtIndex.value
        nodeAtIndex.value = value
        return oldValue


    class Iterator:
        def __init__(self, node):
            self._node = node

        def __next__(self):
            if self._node is None:
                raise StopIteration

            value = self._node.value
            self._node = self._node.next
            return value


    def __iter__(self):
        """Return an iterator"""
        return self.Iterator(self._head)


    @property
    def isEmpty(self):
        return self._head is None
    

    def insertValue(self, value, atIndex):
        assert 0 <= atIndex and atIndex <= len(self), "index out of bounds"
        index = atIndex
        newNode = ADL_SinglyLinkedListNode(value)

        node = self._head

        if index == 0:
            newNode.next = node
            self._head = newNode
        else:
            nodeAtIndex = node
            for i in range(1, index):
                nodeAtIndex = nodeAtIndex.next
            newNode.next = nodeAtIndex.next
            nodeAtIndex.next = newNode


    def appendValue(self, value):
        return self.insertValue(value, len(self))


    def getValue(self, atIndex):
        if self._head is None:
            raise AssertionError("Cannot get item from an empty Collection")
        assert 0 <= atIndex and atIndex < len(self), "index out of bounds"

        return self[atIndex]


    def updateValue(self, value, atIndex):
        if self._head is None:
            raise AssertionError("Cannot update item in an empty Collection")
        assert 0 <= atIndex and atIndex < len(self), "index out of bounds"

        return self.__setitem__(atIndex, value)


    def removeValue(self, atIndex):
        assert 0 <= atIndex and atIndex < len(self), "index out of bounds"
        index = atIndex

        node = self._head

        if index == 0:
            self._head = getattr(node, "next", None)
        else:
            precedingNode = node
            for i in range(1, index):
                precedingNode = precedingNode.next

            node = precedingNode.next
            precedingNode.next = node.next

        return node.value


    def __eq__(self, other):
        if isinstance(other, ADL_SinglyLinkedList) \
            or isinstance(other, list):

            return self.isEqualToOther(other)
            
        raise NotImplementedError


    def isEqualToOther(self, other):
        if len(self) != len(other):
            return False

        for l,r in zip(self, other):
            if l != r:
                return False

        return True

