def long_common_prefix_1(input_list):
    memo = {}

    def addWordToMemo(word, memo):
        for c in word:
            if 'children' not in memo:
                memo['children'] = {}
            if not c in memo['children']:
                memo['children'][c] = {}
            memo = memo['children'][c]
        memo['_isBoundary'] = True

    for w in input_list:
        addWordToMemo(w, memo)

    node = memo

    results = ""

    while('children' in node
        and len(node['children']) == 1
        and '_isBoundary' not in node):

        c = node['children'].keys()[0]
        results += c
        node = node['children'][c]

    return results

def long_common_prefix_2(input_list):
    results = ""
    for i in range(len(input_list[0])):
        c = input_list[0][i]
        isValid = True
        for w in range(1, len(input_list)):
            if i >= len(input_list[w]) or input_list[w][i] != c:
                isValid = False
                break
        if not isValid:
            break
        results += c

    return results





###############################################################################

import unittest

class Test_long_common_prefix_1(unittest.TestCase):

    def test_fire(self):
        i = ['firecode', 'fireacb', 'fireac']
        e = 'fire'
        self.assertEqual(long_common_prefix_1(i), e)

    def test_empty(self):
        i = ['firecode', 'fireacb', 'firac', 'rcafir', 'firecab', 'firecba']
        e = ''
        self.assertEqual(long_common_prefix_1(i), e)

    def test_qir(self):
        i = ['airecode', 'aireacb', 'airac', 'airca', 'airecab', 'airecba']
        e = 'air'
        self.assertEqual(long_common_prefix_1(i), e)

    def test_empty(self):
        i = ['firecode', 'fireacb', 'firac', 'firca', 'firecab', 'firecba']
        e = 'fir'
        self.assertEqual(long_common_prefix_1(i), e)

    def test_short_string_bounds(self):
        i = ['firecode', 'fi', 'fireacb', 'firac', 'firca', 'firecab', 'firecba']
        e = 'fi'
        self.assertEqual(long_common_prefix_1(i), e)



class Test_long_common_prefix_2(unittest.TestCase):

    def test_fire(self):
        i = ['firecode', 'fireacb', 'fireac']
        e = 'fire'
        self.assertEqual(long_common_prefix_2(i), e)

    def test_empty(self):
        i = ['firecode', 'fireacb', 'firac', 'rcafir', 'firecab', 'firecba']
        e = ''
        self.assertEqual(long_common_prefix_2(i), e)

    def test_qir(self):
        i = ['airecode', 'aireacb', 'airac', 'airca', 'airecab', 'airecba']
        e = 'air'
        self.assertEqual(long_common_prefix_2(i), e)

    def test_empty(self):
        i = ['firecode', 'fireacb', 'firac', 'firca', 'firecab', 'firecba']
        e = 'fir'
        self.assertEqual(long_common_prefix_2(i), e)

    def test_short_string_bounds(self):
        i = ['firecode', 'fi', 'fireacb', 'firac', 'firca', 'firecab', 'firecba']
        e = 'fi'
        self.assertEqual(long_common_prefix_2(i), e)

if __name__ == '__main__':
    unittest.main()
