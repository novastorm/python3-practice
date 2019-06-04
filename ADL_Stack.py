from abc import ABCMeta, abstractmethod

from ADL_SinglyLinkedList import *
from ADL_DoublyLinkedList import *

class ADL_Stack:

    @property
    def isEmpty(self):
        raise NotImplementedError
    
    @property
    def count(self):
        raise NotImplementedError

    @property
    def peek(self):
        raise NotImplementedError

    def push(self, value):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError


class ADL_SinglyLinkedList_Stack(ADL_SinglyLinkedList, ADL_Stack):
    @property
    def peek(self):
        return self.head

    def push(self, value):
        self.insert(value, atIndex=0)

    def pop(self):
        if self.isEmpty:
            return None
        return self.remove(atIndex=0)


class ADL_DoublyLinkedList_Stack(ADL_DoublyLinkedList, ADL_Stack):
    @property
    def peek(self):
        return self.last

    def push(self, value):
        self.append(value)

    def pop(self):
        if self.isEmpty:
            return None
        return self.removeLast()

class ADL_List_Stack(list, ADL_Stack):
    @property
    def isEmpty(self):
        return len(self) == 0
    
    @property
    def count(self):
        if self.isEmpty:
            return 0
        return self.__len__()
    

    @property
    def peek(self):
        if self.isEmpty:
            return None
        return self[-1]

    def push(self, value):
        self.append(value)

    def pop(self):
        if self.isEmpty:
            return None
        return super().pop(-1)
