class ADL_SinglyLinkedList:
    """Singly Linked List Implementation"""

    class Node:

        def __init__(self):
            self.next = None
            self.value = None


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


    @property
    def startNode(self):
        return getattr(self, "_startNode", None)
    @startNode.setter
    def startNode(self, newValue):
        self._startNode = newValue


    @property
    def endNode(self):
        return getattr(self, "_endNode", None)
    @endNode.setter
    def endNode(self, newValue):
        self._endNode = newValue


    @property
    def count(self):
        return len(self)

    def __len__(self):
        results = 0
        node = self.startNode
        while node is not None:
            results += 1
            node = node.next
        return results


    @property
    def isEmpty(self):
        return self.startNode is None
    

    @property
    def head(self):
        return getattr(self.startNode, "value", None)


    @property
    def tail(self):
        if self.count < 2:
            return None

        newList = ADL_SinglyLinkedList()
        newList.head = getattr(self.startNode, "next", None)
        return newList
        

    def insert(self, value, atIndex):
        assert 0 <= atIndex and atIndex <= self.count, "index out of bounds"

        index = atIndex

        newNode = self.Node()
        newNode.value = value

        if index == 0:
            newNode.next = self.startNode
            self.startNode = newNode
        else:
            nodeAtIndex = self.startNode
            for i in range(1, index):
                nodeAtIndex = nodeAtIndex.next
            newNode.next = nodeAtIndex.next

            nodeAtIndex.next = newNode


    def getValue(self, atIndex):
        assert 0 <= atIndex and atIndex < self.count, "index out of bounds"
        index = atIndex

        nodeAtIndex = self.startNode
        for i in range(index):
            nodeAtIndex = nodeAtIndex.next

        return nodeAtIndex.value


    def append(self, value):
        self.insert(value, len(self))


    def update(self, value, atIndex):
        assert 0 <= atIndex and atIndex <= self.count, "index out of bounds"
        index = atIndex

        nodeAtIndex = self.startNode
        for i in range(index):
            nodeAtIndex = nodeAtIndex.next

        nodeAtIndex.value = value

    def remove(self, atIndex):
        assert 0 <= atIndex and atIndex < self.count, "index out of bounds"
        index = atIndex

        node = self.startNode
        if index == 0:
            self.startNode = getattr(node, "next", None)
        else:
            precedingNode = self.startNode
            for i in range(1, index):
                precedingNode = getattr(precedingNode, "next", None)
            node = getattr(precedingNode, "next", None)
            if precedingNode is not None:
                precedingNode.next = getattr(node, "next", None)

        return getattr(node, "value", None)

    
    def __getitem__(self, index):
        return self.getValue(index)

    def __setitem__(self, key, value):
        self.update(value, key)


    class Iterator:
        def __init__(self, node):
            self.node = node

        def __iter__(self):
            return self

        def __next__(self):
            if self.node is None:
                raise StopIteration

            value = self.node.value
            self.node = self.node.next
            return value

    def __iter__(self):
        return self.Iterator(self.startNode)

    def __str__(self):
        s = "["
        sep = ""
        for i in self:
            s += sep + str(i)
            sep = ", "
        s += "]"
        return s


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

