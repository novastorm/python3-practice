from abc import ABCMeta, abstractmethod

from ADL_SinglyLinkedList import *
from ADL_DoublyLinkedList import *

class ADL_Queue:

    @property
    def isEmpty(self):
        raise NotImplementedError
    
    def __len__(self):
        raise NotImplementedError

    @property
    def peek(self):
        raise NotImplementedError

    def enqueue(self, value):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError


class ADL_SinglyLinkedList_Queue(ADL_Queue):

    def __init__(self):
        self._list = ADL_SinglyLinkedList()
    

    def __len__(self):
        return len(self._list)


    @property
    def isEmpty(self):
        return len(self) == 0
    

    @property
    def peek(self):
        if self.isEmpty:
            return None
        return self._list[0]


    def enqueue(self, value):
        self._list.appendValue(value)


    def dequeue(self):
        if self.isEmpty:
            return None
        return self._list.removeValue(atIndex=0)


    def __iter__(self):
        return self._list.__iter__()


    def isEqualToOther(self, other):
        if not isinstance(other, ADL_Queue) and not isinstance(other, list):
            raise NotImplementedError

        if len(self) != len(other):
            return False

        for l,r in zip(self, other):
            if l != r: 
                return False

        return True

    def __eq__(self, other):
        return self.isEqualToOther(other)

# class ADL_DoublyLinkedList_Queue(ADL_Queue):
#     @property
#     def peek(self):
#         return self.first

#     def enqueue(self, value):
#         self.append(value)

#     def dequeue(self):
#         if self.isEmpty:
#             return None
#         return self.remove(atIndex=0)


class ADL_List_Queue(ADL_Queue):

    def __init__(self):
        self._list = []
    

    def __len__(self):
        return len(self._list)


    @property
    def isEmpty(self):
        return len(self) == 0
    

    @property
    def peek(self):
        if self.isEmpty:
            return None
        return self._list[0]


    def enqueue(self, value):
        self._list.append(value)


    def dequeue(self):
        if self.isEmpty:
            return None
        return self._list.pop(0)


    def __iter__(self):
        return self._list.__iter__()


    def isEqualToOther(self, other):
        if not isinstance(other, ADL_Queue) and not isinstance(other, list):
            raise NotImplementedError

        if len(self) != len(other):
            return False

        for l,r in zip(self, other):
            if l != r: 
                return False

        return True

    def __eq__(self, other):
        return self.isEqualToOther(other)

