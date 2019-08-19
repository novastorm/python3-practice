class ADL_GraphNode:
    """Graph Node Implementation"""

    def __init__(self, value, numberOfChildren=1):
        self._value = value
        if numberOfChildren < 1:
            return None
        self._children = [None] * numberOfChildren


    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, newValue):
        self._value = newValue


    @property
    def children(self):
        return self._children

