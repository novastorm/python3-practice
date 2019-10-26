def look_and_say(sequence_number):
    if sequence_number < 1:
        return None

    def getSequence(s=None):
        if s is None:
            return "1"

        currentChar = s[0]
        count = 0

        results = ""

        for c in s:
            if c != currentChar:
                results += str(count) + currentChar
                currentChar = c
                count = 1
            else:
                count += 1

        results += str(count) + currentChar

        return results

    results = None

    for i in range(sequence_number):
        results = getSequence(results)

    return results


###############################################################################

import unittest

class Test_look_and_say(unittest.TestCase):

    def test_0(self):
        i = 0
        e = None
        self.assertEqual(look_and_say(i), e)

    def test_1(self):
        i = 1
        e = "1"
        self.assertEqual(look_and_say(i), e)

    def test_3(self):
        i = 3
        e = "21"
        self.assertEqual(look_and_say(i), e)

    def test_5(self):
        i = 5
        e = "111221"
        self.assertEqual(look_and_say(i), e)

    def test_7(self):
        i = 7
        e = "13112221"
        self.assertEqual(look_and_say(i), e)

if __name__ == '__main__':
    unittest.main()
