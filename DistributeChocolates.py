def distributeChocolate(points):
    if not points:
        return 0

    results = [1]

    for i in range(1, len(points)):
        if points[i] > points[i - 1]:
            results.append(results[i - 1] + 1)
        else:
            results.append(1)

    print(results)
    numChoco = results[-1]

    for i in range(len(points) - 2, -1, -1):
        if points[i] > points[i + 1]:
            results[i] = max(results[i], results[i + 1] + 1)

        numChoco += results[i]

    print(results)
    return numChoco


###############################################################################

import unittest


class Test_DistributeChocolate(unittest.TestCase):

    I = 'input'
    E = 'expected'

    def setUp(self):

        I = self.I
        E = self.E

        self.tests = [
            {
                I: [2, 3, 3, 2, 1, 5, 2],
                E: 12
            },
            {
                I: [],
                E: 0
            },
            {
                I: [2],
                E: 1
            },
            {
                I: [1, 5, 7, 1],
                E: 7
            },
            {
                I: [1, 3, 2, 2, 1],
                E: 7
            }
        ]

    def test_0(self):
        I = self.I
        E = self.E

        t = self.tests[0]
        i, e = t[I], t[E]
        self.assertEqual(distributeChocolate(i), e)


    def test_1(self):
        I = self.I
        E = self.E

        t = self.tests[1]
        i, e = t[I], t[E]
        self.assertEqual(distributeChocolate(i), e)

    def test_2(self):
        I = self.I
        E = self.E

        t = self.tests[2]
        i, e = t[I], t[E]
        self.assertEqual(distributeChocolate(i), e)

    def test_3(self):
        I = self.I
        E = self.E

        t = self.tests[3]
        i, e = t[I], t[E]
        self.assertEqual(distributeChocolate(i), e)

    def test_4(self):
        I = self.I
        E = self.E

        t = self.tests[4]
        i, e = t[I], t[E]
        self.assertEqual(distributeChocolate(i), e)

if __name__ == '__main__':
    unittest.main()
