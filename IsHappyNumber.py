def is_happy_number(number):
    memo = set()

    while True:
        if number == 1:
            return True
        if number in memo:
            return False

        memo.add(number)
        number = sumOfSquaresOfDigitsOf(number)

def sumOfSquaresOfDigitsOf(number):
    results = 0
    while number:
        results += (number % 10) * (number % 10)
        number //= 10
    return results

def is_happy_number_2(number):

    if number == 1:
        return True
    if number == 4:
        return False

    number = sumOfSquaresOfDigitsOf(number)
    return is_happy_number_2(number)


# This implementation is incorrect. 7 should evaluation to True
# def is_happy_number_3(number):
#     while True:
#         if number == 1:
#             return True
#         elif number < 10:
#             return False
#         number = sumOfSquaresOfDigitsOf(number)


###############################################################################

import unittest


class Test_is_happy_number(unittest.TestCase):

    def test_1(self):
        i = 1
        e = True
        self.assertEqual(is_happy_number(i), e)

    def test_2(self):
        i = 2
        e = False
        self.assertEqual(is_happy_number(i), e)

    def test_3(self):
        i = 3
        e = False
        self.assertEqual(is_happy_number(i), e)

    def test_4(self):
        i = 4
        e = False
        self.assertEqual(is_happy_number(i), e)

    def test_5(self):
        i = 5
        e = False
        self.assertEqual(is_happy_number(i), e)

    def test_6(self):
        i = 6
        e = False
        self.assertEqual(is_happy_number(i), e)

    def test_7(self):
        i = 7
        e = True
        self.assertEqual(is_happy_number(i), e)

    def test_8(self):
        i = 8
        e = False
        self.assertEqual(is_happy_number(i), e)

    def test_9(self):
        i = 9
        e = False
        self.assertEqual(is_happy_number(i), e)

    def test_68(self):
        i = 68
        e = True
        self.assertEqual(is_happy_number(i), e)

    def test_28(self):
        i = 28
        e = True
        self.assertEqual(is_happy_number(i), e)

    def test_12(self):
        i = 12
        e = False
        self.assertEqual(is_happy_number(i), e)

    def test_100(self):
        i = 100
        e = True
        self.assertEqual(is_happy_number(i), e)


class Test_is_happy_number_2(unittest.TestCase):


    def test_1(self):
        i = 1
        e = True
        self.assertEqual(is_happy_number(i), e)

    def test_2(self):
        i = 2
        e = False
        self.assertEqual(is_happy_number(i), e)

    def test_3(self):
        i = 3
        e = False
        self.assertEqual(is_happy_number(i), e)

    def test_4(self):
        i = 4
        e = False
        self.assertEqual(is_happy_number(i), e)

    def test_5(self):
        i = 5
        e = False
        self.assertEqual(is_happy_number(i), e)

    def test_6(self):
        i = 6
        e = False
        self.assertEqual(is_happy_number(i), e)

    def test_7(self):
        i = 7
        e = True
        self.assertEqual(is_happy_number(i), e)

    def test_8(self):
        i = 8
        e = False
        self.assertEqual(is_happy_number(i), e)

    def test_9(self):
        i = 9
        e = False
        self.assertEqual(is_happy_number(i), e)

    def test_68(self):
        i = 68
        e = True
        self.assertEqual(is_happy_number(i), e)

    def test_28(self):
        i = 28
        e = True
        self.assertEqual(is_happy_number(i), e)

    def test_12(self):
        i = 12
        e = False
        self.assertEqual(is_happy_number(i), e)

    def test_100(self):
        i = 100
        e = True
        self.assertEqual(is_happy_number(i), e)


if __name__ == '__main__':
        unittest.main()
