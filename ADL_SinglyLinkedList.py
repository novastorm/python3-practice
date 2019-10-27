from os import abort

class SinglyLinkedListError(Exception):
    """Base (catch-all) binarytree exception."""
    pass


class SinglyLinkedListNodeTypeError(SinglyLinkedListError):
    """Node was not an instance of :class:`SinglyLinkedListNode`."""
    pass


class SinglyLinkedListNodeValueError(SinglyLinkedListError):
    """Node value was not a valid."""
    pass

class ADL_SinglyLinkedListNode:
    """Singly Linked List Node Implementation"""

    def __init__(self, value):
        self._next = None
        self._value = value


    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, newValue):
        self._value = newValue


    @property
    def next(self):
        return self._next
    @next.setter
    def next(self, newValue):
        self._next = newValue

    @classmethod
    def count(cls, aList):
        """Return the number of nodes in a list"""
        if not isinstance(aList, cls):
            raise TypeError

        results = 0

        while aList:
            results += 1
            aList = aList.next

        return results

    @classmethod
    def hasCycle(cls, aList):
        if not isinstance(aList, ADL_SinglyLinkedListNode):
            return NotImplemented

        slow = aList
        fast = aList

        while fast:
            slow = slow.next
            if not fast.next:
                break
            fast = fast.next.next

            if fast == slow:
                return True

        return False

    @classmethod
    def reverse(cls, aList):
        if not aList:
            return aList

        next = aList
        aList = None

        while next:
            next.next, aList, next = aList, next, next.next

        return aList

    @classmethod
    def findMiddleNode(cls, aList):
        slow = aList
        fast = aList

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = (fast.next).next

        return slow


class ADL_SinglyLinkedList:
    """Singly Linked List Implementation"""

    def __init__(self):
        self._startNode = None
        self._endNode = None
        self._count = 0

    def __len__(self):
        """Return the number of nodes from this node"""
        if self._startNode is None:
            return 0

        return ADL_SinglyLinkedListNode.count(self._startNode)

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

    def insertValueAtIndex(self, value, index):
        assert 0 <= index and index <= len(self), "index out of bounds"

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

        if self._endNode:
            self._endNode.next = newNode

        self._endNode = newNode

    def getValueAtIndex(self, index):
        if self._startNode is None:
            raise AssertionError("Cannot get item from an empty Collection")
        assert 0 <= index and index < len(self), "index out of bounds"

        return self[index]

    def updateValueAtIndex(self, value, index):
        if self._startNode is None:
            raise AssertionError("Cannot update item in an empty Collection")
        assert 0 <= index and index < len(self), "index out of bounds"

        return self.__setitem__(index, value)

    def removeValueAtIndex(self, index):
        assert 0 <= index and index < len(self), "index out of bounds"

        node = self._startNode

        if index == 0:
            self._startNode = getattr(node, "next", None)
            if index == len(self) - 1:
                self._endNode = None
        else:
            precedingNode = node
            for i in range(1, index):
                precedingNode = precedingNode.next

            node = precedingNode.next
            precedingNode.next = node.next

            if index == len(self) - 1:
                self._endNode = precedingNode

        return node.value

    def __eq__(self, other):
        if isinstance(other, ADL_SinglyLinkedList) or isinstance(other, list):
            return self.isEqualToOther(other)

        raise NotImplementedError

    def isEqualToOther(self, other):
        if len(self) != len(other):
            return False

        for left, right in zip(self, other):
            if left != right:
                return False

        return True
