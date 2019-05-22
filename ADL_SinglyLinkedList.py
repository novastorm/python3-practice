class ADL_SinglyLinkedList:
    """Singly Linked List Implementation"""

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
    def count(self):
        return (1 if self.value is not None else 0) + (self.next.count if self.next is not None else 0)

    def __len__(self):
        return self.count

    @property
    def isEmpty(self):
        return self.count == 0
    
    
    @property
    def head(self):
        return self.next.value if self.next is not None else None


    @property
    def tail(self):
        if self.count < 2:
            return None

        newList = ADL_SinglyLinkedList()
        newList.next = self.next.next if self.next is not None else None
        return newList
        

    def insert(self, value, atIndex):
        assert 0 <= atIndex and atIndex <= self.count, "index out of bounds"

        index = atIndex

        newNode = ADL_SinglyLinkedList()
        newNode.value = value

        if index == 0:
            newNode.next = self.next
            self.next = newNode
        else:
            nodeAtIndex = self.next
            for i in range(1, index):
                nodeAtIndex = nodeAtIndex.next
            newNode.next = getattr(nodeAtIndex, "next", None)

            nodeAtIndex.next = newNode


    def append(self, value):
        self.insert(value, self.count)


    def update(self, value, atIndex):
        assert 0 <= atIndex and atIndex <= self.count, "index out of bounds"
        index = atIndex

        nodeAtIndex = self.next
        for i in range(index):
            nodeAtIndex = nodeAtIndex.next

        nodeAtIndex.value = value


    def __setitem__(self, key, value):
        self.update(value, key)


    def getValue(self, atIndex):
        assert 0 <= atIndex and atIndex < self.count, "index out of bounds"
        index = atIndex

        nodeAtIndex = self.next
        for i in range(index):
            nodeAtIndex = nodeAtIndex.next

        return nodeAtIndex.value

    
    def __getitem__(self, index):
        return self.getValue(index)


    class Iterator:
        def __init__(self, aList):
            self.list = aList

        def __iter__(self):
            return self

        def __next__(self):
            if self.list is None:
                raise StopIteration

            value = self.list.value
            self.list = self.list.next
            return value

    def __iter__(self):
        return self.Iterator(self.next)

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

    def remove(self, atIndex):
        assert 0 <= atIndex and atIndex < self.count, "index out of bounds"
        index = atIndex

        node = self.next
        if index == 0:
            self.next = node.next if node is not None else None
        else:
            precedingNode = self.next
            for i in range(1, index):
                precedingNode = precedingNode.next if precedingNode is not None else None
            node = precedingNode.next if precedingNode is not None else None
            if precedingNode is not None:
                precedingNode.next = node.next if node is not None else None

        return node.value if node is not None else None

