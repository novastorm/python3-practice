class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    class SinglyLinkedListNodeIterator:
        def __init__(self, lst):
            self.lst = lst

        def __iter__(self):
            return self

        def __next__(self):
            if not self.lst:
                raise StopIteration

            next = self.lst

            self.lst = next.next

            return next.data

        next = __next__

    def __iter__(self):
        return self.SinglyLinkedListNodeIterator(self)


class SinglyLinkedList:
    def __init__(self):
        '''
        constructor
        '''
        self.head = None

    def setHead(self, head):
        '''
        method for setting the head of the Linked List
        '''
        self.head = head

    def arrange_in_pairs(self):
        if not self.head:
            return self.head

        def splitListIntoHalves(aList):
            slow = aList
            fast = aList

            while fast:
                if not fast.next:
                    break
                slow = slow.next
                fast = fast.next.next

            lower = aList
            upper = slow.next
            slow.next = None

            return lower, upper

        def reverseList(aList):
            if not aList:
                return aList

            next = aList
            aList = None

            while next:
                next.next, aList, next = aList, next, next.next

            return aList

        def mergeLists(listA, listB):
            print "listA", list(iter(listA)) if listA else None
            print "listB", list(iter(listB)) if listB else None
            print "lA:", listA.data if listA else None
            print "lB:", listB.data if listB else None

            results = listA

            next, listA = listA, listA.next
            if listB:
                next.next, listB = listB, listB.next
                next = next.next

            print "results", list(iter(results))

            while listA or listB:
                print "lA:", listA.data if listA else None
                print "lB:", listB.data if listB else None

                next.next, listA = listA, listA.next
                next = next.next
                if listB:
                    next.next, listB = listB, listB.next
                    next = next.next
                print "results", list(iter(results))

            return results


        lower, upper = splitListIntoHalves(self.head)
        upper = reverseList(upper)
        results = mergeLists(lower, upper)

        print "final", list(iter(results))
        self.head = results
        return self.head

    def __iter__(self):
        return self.head


###############################################################################

import unittest


class Test_arrange_in_pairs_1(unittest.TestCase):

    def test_no_list(self):
        aList = SinglyLinkedList()
        h = None
        aList.setHead(h)
        i = aList.arrange_in_pairs()
        e = None
        self.assertEqual(i, e)

    def test_one_element_list(self):
        aList = SinglyLinkedList()
        h = Node(1)
        aList.setHead(h)
        aList.arrange_in_pairs()
        i = list(iter(aList))
        e = [1]
        self.assertEqual(i, e)

    def test_odd_length_list(self):
        aList = SinglyLinkedList()
        h = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        aList.setHead(h)
        aList.arrange_in_pairs()
        i = list(iter(aList))
        e = [1, 5, 2, 4, 3]
        self.assertEqual(i, e)

    def test_even_length_list(self):
        aList = SinglyLinkedList()
        h = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
        aList.setHead(h)
        aList.arrange_in_pairs()
        i = list(iter(aList))
        e = [1, 6, 2, 5, 3, 4]
        self.assertEqual(i, e)


if __name__ == '__main__':
    unittest.main()
