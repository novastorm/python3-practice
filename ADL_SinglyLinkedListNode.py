from os import abort

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


    def __len__(self):
        """Return the number of nodes from this node"""
        if self.next is None:
            return 1

        return 1 + self.next.__len__()


    # def __str__(self):
    #     """Return the string description of this list"""
    #     s = "["
    #     sep = ""
    #     for i in self:
    #         s += sep + str(i)
    #         sep = ", "
    #     s += "]"
    #     return s


    # def __getitem__(self, index):
    #     assert 0 <= index and index < len(self), "index out of bounds"

    #     nodeAtIndex = self
    #     for i in range(index):
    #         nodeAtIndex = nodeAtIndex.next

    #     return nodeAtIndex

    # def __setitem__(self, key, value):
    #     assert 0 <= index and index < len(self), "index out of bounds"

    #     nodeAtIndex = self
    #     for i in range(index):
    #         nodeAtIndex = nodeAtIndex.next

    #     oldValue = nodeAtIndex.value
    #     nodeAtIndex.value = value
    #     return oldValue


    # class Iterator:
    #     def __init__(self, node):
    #         self._node = node

    #     def __next__(self):
    #         if self._node is None:
    #             raise StopIteration

    #         value = self._node.value
    #         self._node = self._node.next
    #         return value


    # def __iter__(self):
    #     """Return an iterator"""
    #     return self.Iterator(self)


    # @staticmethod
    # def len(aList):
    #     if aList is None:
    #         return 0
    #     return aList.__len__()


    # @staticmethod
    # def isEmpty(aList):
    #     return aList is None
    

    # @staticmethod
    # def insertNode(aList, newNode, atIndex):
    #     count = ADL_SinglyLinkedList.len(aList)
    #     assert 0 <= atIndex and atIndex <= count, "index out of bounds"
    #     index = atIndex

    #     if index == 0:
    #         newNode.next = aList
    #         aList = newNode
    #     else:
    #         nodeAtIndex = aList
    #         for i in range(1, index):
    #             nodeAtIndex = nodeAtIndex.next
    #         newNode.next = nodeAtIndex.next
    #         nodeAtIndex.next = newNode

    #     return aList


    # @staticmethod
    # def appendNode(aList, newNode):
    #     count = ADL_SinglyLinkedList.len(aList) or 0
    #     return ADL_SinglyLinkedList.insertNode(aList, newNode, count)

    # @staticmethod
    # def getNode(aList, atIndex):
    #     if aList is None:
    #         raise AssertionError("Cannot get item from an empty Collection")
    #     assert 0 <= atIndex and atIndex < len(self), "index out of bounds"
    #     index = atIndex

    #     nodeAtIndex = self
    #     for i in range(index):
    #         nodeAtIndex = nodeAtIndex.next

    #     return nodeAtIndex


    # @staticmethod
    # def removeNode(aList, atIndex):
    #     count = ADL_SinglyLinkedList.len(aList) or 0
    #     assert 0 <= atIndex and atIndex < count, "index out of bounds"
    #     index = atIndex

    #     node = aList

    #     if index == 0:
    #         aList = getattr(node, "next", None)
    #     else:
    #         precedingNode = aList
    #         for i in range(1, index):
    #             precedingNode = precedingNode.next

    #         node = precedingNode.next
    #         precedingNode.next = node.next

    #         # if index == self.count:
    #         #     self.endNode = precedingNode

    #     return (aList, node)


    # @property
    # def tail(self):
    #     if self.count < 2:
    #         return None

    #     newList = ADL_SinglyLinkedList()
    #     newList.head = getattr(self.startNode, "next", None)
    #     return newList
        

    # def __eq__(self, other):
    #     if isinstance(other, ADL_SinglyLinkedList) \
    #         or isinstance(other, list):

    #         return self.isEqualToOther(other)
            
    #     raise NotImplementedError


    # def isEqualToOther(self, other):
    #     if len(self) != len(other):
    #         return False

    #     for l,r in zip(self, other):
    #         if l != r:
    #             return False

    #     return True

