class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next


class SinglyLinkedList:
    # constructor
    def __init__(self, head=None):
        self.head = head

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def find_nth_node_from_end(self, n):
        return self.find_nth_node_from_end_3(n)

    def find_nth_node_from_end_1(self, n):
        '''
        Traverse the list to find its length. Calculate the nuumber of steps to
        the target node position. Traverse the list by number of steps to reach
        the tartget position.

        Time: O(2n) Linear
        Space: O(1) Constant
        '''
        if not self.head or not n or n < 0:
            return None
        length = 0
        curr = self.head
        while curr:
            length += 1
            curr = curr.next

        if n > length:
            return None

        t = length - n
        # print(t)
        curr = self.head
        for i in range(t):
            # print(i)
            curr = curr.next

        return curr

    def find_nth_node_from_end_2(self, n):
        '''
        Use fast and slow walklers to traverse the list. Once fast finds the
        end of the list, fast position contains its length.

        Calculate the number of steps to the target node. If the target node
        position is less that then the slow position, reset slow and slow
        position.

        Increment slow position and slow reference to the target positon.

        Time: O(n) Linear
        Space: O(1) Constant
        '''
        if not self.head or not n or n < 0:
            return None

        slowPosition = 0
        fastPosition = 0
        
        slow = self.head
        fast = self.head
        
        while fast:
            slow = slow.next
            slowPosition += 1
            
            if not fast.next:
                fastPosition += 1
                break
            
            fast = fast.next.next
            fastPosition += 2
            
        # print(slowPosition, fastPosition)
        if n > fastPosition:
            return None
        t = fastPosition - n
        # print("t", t)

        if t < slowPosition:
            slowPosition = 0
            slow = self.head

        while slowPosition < t:
            slowPosition += 1
            slow = slow.next

        return slow


    def find_nth_node_from_end_3(self, n):
        '''
        Designate a lead and tail references. Advance lead N positions.

        Return None if lead becomes None before advancing N positions.

        Advance lead and tail until lead reaches the end of the list. Tail is
        t the target node.

        Time: O(n) Linear
        Space: O(1) Constant
        '''
        if not self.head or not n or n < 0:
            return None

        lead = self.head
        tail = self.head

        for i in range(n):
            if lead is None:
                # n is longer than number of nodes in list
                return None
            lead = lead.next

        while lead:
            lead = lead.next
            tail = tail.next

        return tail

###############################################################################

import unittest


class Test_DistributeChocolate(unittest.TestCase):

    def setUp(self):
        pass

    def test_1_0(self):
        i = SinglyLinkedList(Node(1, Node(2, Node(3, Node(4)))))
        k = 2
        e = 3
        node = i.find_nth_node_from_end_1(k)
        self.assertEqual(node.data if node else None, e)

    def test_1_1(self):
        i = SinglyLinkedList(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))))
        k = 3
        e = 4
        node = i.find_nth_node_from_end_1(k)
        self.assertEqual(node.data if node else None, e)

    def test_1_2(self):
        i = SinglyLinkedList(Node(1, Node(2, Node(3, Node(4)))))
        k = -1
        e = None
        node = i.find_nth_node_from_end_1(k)
        self.assertEqual(node.data if node else None, e)

    def test_1_3(self):
        i = SinglyLinkedList()
        k = None
        e = None
        node = i.find_nth_node_from_end_1(k)
        self.assertEqual(node.data if node else None, e)

    def test_1_4(self):
        i = SinglyLinkedList(Node(1, Node(2, Node(3, Node(4)))))
        k = 10
        e = None
        node = i.find_nth_node_from_end_1(k)
        self.assertEqual(node.data if node else None, e)


    def test_2_0(self):
        i = SinglyLinkedList(Node(1, Node(2, Node(3, Node(4)))))
        k = 2
        e = 3
        node = i.find_nth_node_from_end_2(k)
        self.assertEqual(node.data if node else None, e)

    def test_2_1(self):
        i = SinglyLinkedList(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))))
        k = 3
        e = 4
        node = i.find_nth_node_from_end_2(k)
        self.assertEqual(node.data if node else None, e)

    def test_2_2(self):
        i = SinglyLinkedList(Node(1, Node(2, Node(3, Node(4)))))
        k = -1
        e = None
        node = i.find_nth_node_from_end_2(k)
        self.assertEqual(node.data if node else None, e)

    def test_2_3(self):
        i = SinglyLinkedList()
        k = None
        e = None
        node = i.find_nth_node_from_end_2(k)
        self.assertEqual(node.data if node else None, e)

    def test_2_4(self):
        i = SinglyLinkedList(Node(1, Node(2, Node(3, Node(4)))))
        k = 10
        e = None
        node = i.find_nth_node_from_end_2(k)
        self.assertEqual(node.data if node else None, e)


    def test_3_0(self):
        i = SinglyLinkedList(Node(1, Node(2, Node(3, Node(4)))))
        k = 2
        e = 3
        node = i.find_nth_node_from_end_3(k)
        self.assertEqual(node.data if node else None, e)

    def test_3_1(self):
        i = SinglyLinkedList(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))))
        k = 3
        e = 4
        node = i.find_nth_node_from_end_3(k)
        self.assertEqual(node.data if node else None, e)

    def test_3_2(self):
        i = SinglyLinkedList(Node(1, Node(2, Node(3, Node(4)))))
        k = -1
        e = None
        node = i.find_nth_node_from_end_3(k)
        self.assertEqual(node.data if node else None, e)

    def test_3_3(self):
        i = SinglyLinkedList()
        k = None
        e = None
        node = i.find_nth_node_from_end_3(k)
        self.assertEqual(node.data if node else None, e)

    def test_3_4(self):
        i = SinglyLinkedList(Node(1, Node(2, Node(3, Node(4)))))
        k = 10
        e = None
        node = i.find_nth_node_from_end_3(k)
        self.assertEqual(node.data if node else None, e)

if __name__ == '__main__':
    unittest.main()
