def maximumStockProfit(prices, fee):
    return maximumStockProfit_1(prices, fee)

def maximumStockProfit_1(prices, fee):
    # max profit
    mp = 0
    # max delta
    md = -prices[0]

    for p in prices:
        # gain
        g = md + p - fee
        mp = max(mp, g)

        # max price to price delta
        d = mp - p
        md = max(md, d)

    return mp

def maximumStockProfit_2(prices, fee):
    m = 0
    h = 0

    for i in range(1, len(prices)):
        g = prices[i] - prices[i - 1]
        m, h = max(m, h + g - fee), max(m, h + g)

    return m

def maximumStockProfit_3(prices, fee):
    rp = 0 # realized profit
    up = 0 # unrealized profit

    for i in range(1, len(prices)):
        # difference
        d = prices[i] - prices[i - 1]

        # unrealized gain
        ug = up + d
        # realized gain
        rg = up + d - fee

        rp = max(rp, rg)
        up = max(rp, ug)

    return rp

###############################################################################

import unittest

class Test_Maximum_Stock_Profit(unittest.TestCase):

    S = 'stock'
    F = 'fee'
    E = 'expected'

    def setUp(self):
        S = self.S
        F = self.F
        E = self.E

        self.tests = [
            {
                S: [1, 2],
                F: 2,
                E: 0
            },
            {
                S: [1, 3, 2],
                F: 2,
                E: 0
            },
            {
                S: [1, 3, 2, 8],
                F: 2,
                E: 5
            },
            {
                S: [1, 3, 2, 8, 4, 10, 3],
                F: 2,
                E: 9
            },
            {
                S: [1, 3, 2, 8, 4, 10, 3, 7],
                F: 2,
                E: 11
            },
            {
                S: [1, 3, 2, 8, 4, 10, 3, 7, 11],
                F: 2,
                E: 15
            },
        ]

    def test_maximumStockProfit_1(self):
        S = self.S
        F = self.F
        E = self.E

        for t in self.tests:
            s, f, e = t[S], t[F], t[E]
            self.assertEqual(maximumStockProfit_1(s, f), e, (s, f, e))

    def test_maximumStockProfit_2(self):
        S = self.S
        F = self.F
        E = self.E

        for t in self.tests:
            s, f, e = t[S], t[F], t[E]
            self.assertEqual(maximumStockProfit_2(s, f), e, (s, f, e))

    def test_maximumStockProfit_3(self):
        S = self.S
        F = self.F
        E = self.E

        for t in self.tests:
            s, f, e = t[S], t[F], t[E]
            self.assertEqual(maximumStockProfit_3(s, f), e, (s, f, e))

if __name__ == '__main__':

    unittest.main()
