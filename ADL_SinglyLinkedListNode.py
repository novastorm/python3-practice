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


    @staticmethod
    def hasCycle(aList):
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

    @staticmethod
    def reverse(aList):
        if not aList:
            return aList
                
        next = aList
        aList = None
        
        while next:
            next.next, aList, next = aList, next, next.next
        
        return aList

