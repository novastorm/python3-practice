'''
Given a singly-linked list, reverse the list. This can be done
iteratively or recursively. Can you get both solutions?

Example:
Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def printList(self):
        node = self
        output = ''
        sep = ''
        while node is not None:
            output += sep
            output += str(node.val)
            sep = '\040'
            node = node.next
        return output

    # Iterative Solution
    def reverseIteratively(self, head):
        # Implement this.
        newHead = None
        currNode = head

        while currNode:
            nextNode = currNode.next
            currNode.next = newHead
            newHead = currNode

            currNode = nextNode

        return newHead

    # Recursive Solution
    def reverseRecursively(self, head):
        # Implement this.
        def helper(headNode, prevNode=None):
            if headNode is None:
                return prevNode

            nextNode = headNode.next
            headNode.next = prevNode

            return helper(nextNode, headNode)

        return helper(head)

###############################################################################

import unittest
# from ReverseASinglyLinkedList import *


class Test_ReverseASinglyLinkedList(unittest.TestCase):

    def setUp(self):
        node4 = ListNode(4)
        node3 = ListNode(3)
        node2 = ListNode(2)
        node1 = ListNode(1)
        node0 = ListNode(0)

        node4.next = node3
        node3.next = node2
        node2.next = node1
        node1.next = node0

        self.head = node4
        self.last = node0

    def test_reverseIteratively(self):
        self.head.reverseIteratively(self.head)
        self.assertEqual(self.last.printList(), "0 1 2 3 4")

    def test_reverseRecursively(self):
        self.head.reverseRecursively(self.head)
        self.assertEqual(self.last.printList(), "0 1 2 3 4")


if __name__ == '__main__':
        unittest.main()
