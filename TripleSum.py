def triple_sum(integer_list, target_number):
    if not integer_list:
        return []

    def double_sum(integer_list, target_number):
        memo = set()
        results = []
        for n in integer_list:
            t = target_number - n
            if t in memo:
                results.append((t, n))
                memo.remove(t)
            else:
                memo.add(n)
        return results
        
    results = set()
    for i in range(len(integer_list)-2):
        n = integer_list[i]
        t = target_number - n
        ds = double_sum(integer_list[i+1:], t)
        for rA, rB in ds:
            results.add((n, rA, rB))
            
    return list(results)


###############################################################################

import unittest

class Test_triple_sum(unittest.TestCase):

    def test_empty(self):
        l = []
        t = 0
        e = []
        ri = set(triple_sum(l, t))
        re = set(e)
        self.assertEqual(ri, re)

    def test_1(self):
        l = [1,2,3,4,5,6,7,8]
        t = 20
        e = [(5, 7, 8)]
        ri = set(triple_sum(l, t))
        re = set(e)
        self.assertEqual(ri, re)

    def test_2(self):
        l = [1,2,3,4,5,6,7]
        t = 10
        e = [(1, 2, 7), (1, 3, 6), (1, 4, 5), (2, 3, 5)]
        ri = set(triple_sum(l, t))
        re = set(e)
        self.assertEqual(ri, re)

    def test3(self):
        l = [-2,-1,0,0,1,2]
        t = 0
        e = [(-2, 0, 2), (-1, 0, 1)]
        ri = set(triple_sum(l, t))
        re = set(e)
        self.assertEqual(ri, re)

    def test_4(self):
        l = [1,1,1]
        t = 3
        e = [(1, 1, 1)]
        ri = set(triple_sum(l, t))
        re = set(e)
        self.assertEqual(ri, re)

    def test_5(self):
        l = [1,2,3,4,5,6,7]
        t = 15
        e = [(2, 6, 7), (3, 5, 7), (4, 5, 6)]
        ri = set(triple_sum(l, t))
        re = set(e)
        self.assertEqual(ri, re)

if __name__ == '__main__':
    unittest.main()
