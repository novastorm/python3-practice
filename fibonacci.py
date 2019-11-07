class Fibonacci:
    @staticmethod
    def recursive_top_down(n):
        assert 0 <= n, "positive integers only"

        def helper(n):

            if n < 2:
                return n

            return helper(n - 1) + helper(n - 2)

        return helper(n)

    @staticmethod
    def recursive_top_down_memoized(n):
        assert 0 <= n, "positive integers only"

        memo = {}

        def helper(n, memo=memo):

            if n in memo:
                return memo[n]

            if n < 2:
                results = n
            else:
                results = helper(n - 1) + helper(n - 2)

            memo[n] = results

            return results

        return helper(n)

    @staticmethod
    def recursive_bottom_up_memoized(n):
        assert 0 <= n, "positive integers only"

        memo = {}

        def helper(i=0, n=n, memo=memo):

            if i < 2:
                results = i
            else:
                results = memo[i - 1] + memo[i - 2]

            memo[i] = results

            if i < n:
                return helper(i + 1)
            else:
                return results

        return helper()

    @staticmethod
    def iterative_bottom_up_memoized(n):
        assert 0 <= n, "positive integers only"

        memo = {}

        for i in range(n + 1):

            if i < 2:
                results = i
            else:
                results = memo[i - 1] + memo[i - 2]

            memo[i] = results

        return results

    @staticmethod
    def recursive_bottom_up_memoized_space_efficient(n):
        assert 0 <= n, "positive integers only"

        def helper(n, next=1, curr=0):

            if n < 1:
                return curr
            else:
                return helper(n - 1, curr + next, next)

        return helper(n)

    @staticmethod
    def iterative_bottom_up_memoized_space_efficient(n):
        assert 0 <= n, "positive integers only"

        next, curr = 1, 0

        for i in range(n):
            next, curr = curr + next, next

        return curr

    @staticmethod
    def formula(n):
        assert 0 <= n, "positive integers only"

        if n == 0 or n == 1:
            return n

        import math
        phi_1 = (math.sqrt(5) + 1) / 2
        phi_2 = (math.sqrt(5) - 1) / 2
        f = (phi_1**n - phi_2**n) / math.sqrt(5)

        return round(f)

###############################################################################

import unittest


class Test_Fibonacci(unittest.TestCase):

    def test_recursive_top_down(self):
        f = Fibonacci.recursive_top_down
        with self.assertRaises(AssertionError):
            f(-1)
        self.assertEqual(f(0), 0)
        self.assertEqual(f(1), 1)
        self.assertEqual(f(2), 1)
        self.assertEqual(f(3), 2)
        self.assertEqual(f(4), 3)
        self.assertEqual(f(5), 5)
        self.assertEqual(f(10), 55)

    def test_recursive_top_down_memoized(self):
        f = Fibonacci.recursive_top_down_memoized
        with self.assertRaises(AssertionError):
            f(-1)
        self.assertEqual(f(0), 0)
        self.assertEqual(f(1), 1)
        self.assertEqual(f(2), 1)
        self.assertEqual(f(3), 2)
        self.assertEqual(f(4), 3)
        self.assertEqual(f(5), 5)
        self.assertEqual(f(10), 55)

    def test_recursive_bottom_up_memoized(self):
        f = Fibonacci.recursive_bottom_up_memoized
        with self.assertRaises(AssertionError):
            f(-1)
        self.assertEqual(f(0), 0)
        self.assertEqual(f(1), 1)
        self.assertEqual(f(2), 1)
        self.assertEqual(f(3), 2)
        self.assertEqual(f(4), 3)
        self.assertEqual(f(5), 5)
        self.assertEqual(f(10), 55)

    def test_iterative_bottom_up_memoized(self):
        f = Fibonacci.iterative_bottom_up_memoized
        with self.assertRaises(AssertionError):
            f(-1)
        self.assertEqual(f(0), 0)
        self.assertEqual(f(1), 1)
        self.assertEqual(f(2), 1)
        self.assertEqual(f(3), 2)
        self.assertEqual(f(4), 3)
        self.assertEqual(f(5), 5)
        self.assertEqual(f(10), 55)

    def test_recursive_bottom_up_memoized_space_efficient(self):
        f = Fibonacci.recursive_bottom_up_memoized_space_efficient
        with self.assertRaises(AssertionError):
            f(-1)
        self.assertEqual(f(0), 0)
        self.assertEqual(f(1), 1)
        self.assertEqual(f(2), 1)
        self.assertEqual(f(3), 2)
        self.assertEqual(f(4), 3)
        self.assertEqual(f(5), 5)
        self.assertEqual(f(10), 55)

    def test_iterative_bottom_up_memoized_space_efficient(self):
        f = Fibonacci.iterative_bottom_up_memoized_space_efficient
        with self.assertRaises(AssertionError):
            f(-1)
        self.assertEqual(f(0), 0)
        self.assertEqual(f(1), 1)
        self.assertEqual(f(2), 1)
        self.assertEqual(f(3), 2)
        self.assertEqual(f(4), 3)
        self.assertEqual(f(5), 5)
        self.assertEqual(f(10), 55)

    def test_formula(self):
        f = Fibonacci.formula
        with self.assertRaises(AssertionError):
            f(-1)
        self.assertEqual(f(0), 0)
        self.assertEqual(f(1), 1)
        self.assertEqual(f(2), 1)
        self.assertEqual(f(3), 2)
        self.assertEqual(f(4), 3)
        self.assertEqual(f(5), 5)
        self.assertEqual(f(10), 55)


if __name__ == '__main__':
    unittest.main()
