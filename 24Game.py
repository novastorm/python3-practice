from itertools import permutations

class Solution(object):
    def judgePoint24(nums):
        operators = [
            lambda a, b: a * b, 
            lambda a, b: (float(a) / b) if b != 0 else None,
            lambda a, b: a + b,
            lambda a, b: a - b
        ]
        
        def solve(nums):
            # node has one element. Nothing to compute, just yield it
            if len(nums) == 1:
                yield nums[0]
                return

            # divide remaining numbers into left and right half
            for pnums in permutations(nums): 
                for i in range(1, len(pnums)):
                    for left in solve(pnums[:i]):
                        if not left:
                            continue
                        for right in solve(pnums[i:]):
                            if not right:
                                continue
                            for operator in operators:
                                yield operator(left, right)
                            
        for result in solve(nums):
            if abs(result - 24) < 1e-6:
                return True
        return False



###############################################################################

import unittest
from random import randrange

class Test_EvaluateInorderExpression(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        inputVal = []
        for i in range(4):
            inputVal.append(randrange(13) + 1)
        print(inputVal)
        print(Solution.judgePoint24(inputVal))


if __name__ == '__main__':
        unittest.main()        