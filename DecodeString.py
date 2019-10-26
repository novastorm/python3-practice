def decode_string_recursive_1(msg, debug=False):
    if debug:
        print(msg)

    if len(msg) == 1:
        if int(msg) == 0:
            return 0
        return 1

    if int(msg[:1]) == 0:
        A =  0
    else:
        A = decode_string_recursive_1(msg[1:], debug)


    if int(msg[:2]) > 26:
        B = 0
    else:
        if len(msg) == 2:
            B = 1
        else:
            B = decode_string_recursive_1(msg[2:], debug)

    return A + B
    
def decode_string_recursive_2(msg, debug=False):
    if debug:
        print(msg)

    if msg[:1] == '0':
        return 0

    if len(msg) == 1:
        return 1

    A = decode_string_recursive_2(msg[1:], debug)

    if int(msg[:2]) > 26:
        B = 0
    elif len(msg) == 2:
        B = 1
    else:
        B = decode_string_recursive_2(msg[2:], debug)

    return A + B
    


###############################################################################

import unittest


class Test_DecodeString(unittest.TestCase):

    I = 'input'
    E = 'expected'

    def setUp(self):
        pass

    def test_0_1(self):
        i = '113021'
        e = 0
        self.assertEqual(decode_string_recursive_1(i), e)

    def test_0_2(self):
        i = '113021'
        e = 0
        self.assertEqual(decode_string_recursive_2(i), e)

    def test_1(self):
        i = '21234'
        e = 5
        self.assertEqual(decode_string_recursive_2(i), e)

    def test_2(self):
        i = '521'
        e = 2
        self.assertEqual(decode_string_recursive_2(i), e)

    def test_3(self):
        i = '29'
        e = 1
        self.assertEqual(decode_string_recursive_2(i), e)

    def test_4(self):
        i = '2202'
        e = 1
        self.assertEqual(decode_string_recursive_2(i), e)

if __name__ == '__main__':
    unittest.main()
