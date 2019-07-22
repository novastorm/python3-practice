from os import abort
from ADL_SinglyLinkedListNode import *

class ADL_SinglyLinkedList:
    """Singly Linked List Implementation"""

    def __init__(self):
        self._startNode = None
        self._endNode = None


    def __len__(self):
        """Return the number of nodes from this node"""
        if self._startNode is None:
            return 0

        return len(self._startNode)


    def __str__(self):
        """Return the string description of this list"""
        s = "["
        sep = ""
        for i in self._startNode:
            s += sep + str(i)
            sep = ", "
        s += "]"
        return s


    def __getitem__(self, index):
        assert 0 <= index and index < len(self), "index out of bounds"

        nodeAtIndex = self._startNode
        for i in range(index):
            nodeAtIndex = nodeAtIndex.next

        return nodeAtIndex.value

    def __setitem__(self, index, value):
        assert 0 <= index and index < len(self), "index out of bounds"

        nodeAtIndex = self._startNode
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
        return self.Iterator(self._startNode)


    @property
    def isEmpty(self):
        return self._startNode is None
    

    def insertValue(self, value, atIndex):
        assert 0 <= atIndex and atIndex <= len(self), "index out of bounds"
        index = atIndex
        newNode = ADL_SinglyLinkedListNode(value)

        node = self._startNode


        if index == len(self):
            self.appendValue(value)
        elif index == 0:
            newNode.next = node
            self._startNode = newNode
        else:
            nodeAtIndex = node
            for i in range(1, index):
                nodeAtIndex = nodeAtIndex.next
            newNode.next = nodeAtIndex.next
            nodeAtIndex.next = newNode


    def appendValue(self, value):
        newNode = ADL_SinglyLinkedListNode(value)

        if self.isEmpty:
            self._startNode = newNode

        if self._endNode != None:
            self._endNode.next = newNode

        self._endNode = newNode


    def getValue(self, atIndex):
        if self._startNode is None:
            raise AssertionError("Cannot get item from an empty Collection")
        assert 0 <= atIndex and atIndex < len(self), "index out of bounds"

        return self[atIndex]


    def updateValue(self, value, atIndex):
        if self._startNode is None:
            raise AssertionError("Cannot update item in an empty Collection")
        assert 0 <= atIndex and atIndex < len(self), "index out of bounds"

        return self.__setitem__(atIndex, value)


    def removeValue(self, atIndex):
        assert 0 <= atIndex and atIndex < len(self), "index out of bounds"
        index = atIndex

        node = self._startNode

        if index == 0:
            self._startNode = getattr(node, "next", None)
            if index == len(self)-1:
                self._endNode = None
        else:
            precedingNode = node
            for i in range(1, index):
                precedingNode = precedingNode.next

            node = precedingNode.next
            precedingNode.next = node.next

            if index == len(self)-1:
                self._endNode = precedingNode

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

