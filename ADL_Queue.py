from abc import ABCMeta, abstractmethod

from ADL_SinglyLinkedList import *
from ADL_DoublyLinkedList import *

class ADL_Queue:

    @property
    def isEmpty(self):
        raise NotImplementedError
    
    @property
    def count(self):
        raise NotImplementedError

    @property
    def peek(self):
        raise NotImplementedError

    def enqueue(self, value):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError


class ADL_SinglyLinkedList_Queue(ADL_SinglyLinkedList, ADL_Queue):
    @property
    def peek(self):
        return self.head

    def enqueue(self, value):
        self.append(value)

    def dequeue(self):
        if self.isEmpty:
            return None
        return self.remove(atIndex=0)


class ADL_DoublyLinkedList_Queue(ADL_DoublyLinkedList, ADL_Queue):
    @property
    def peek(self):
        return self.first

    def enqueue(self, value):
        self.append(value)

    def dequeue(self):
        if self.isEmpty:
            return None
        return self.remove(atIndex=0)

class ADL_List_Queue(list, ADL_Queue):
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
        return self[0]

    def enqueue(self, value):
        self.append(value)

    def dequeue(self):
        if self.isEmpty:
            return None
        return super().pop(0)
