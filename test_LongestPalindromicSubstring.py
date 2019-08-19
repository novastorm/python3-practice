import unittest
from LongestPalindromicSubstring import *

class Test_LongestPalindromicSubstring(unittest.TestCase):

    def test_bruteforce(self):
        self.assertEqual(LongestPalindromicSubstring.bruteforce("babad"), "bab")
        self.assertEqual(LongestPalindromicSubstring.bruteforce("a"), "a")
        self.assertEqual(LongestPalindromicSubstring.bruteforce("ac"), "a")

    def test_recursive(self):
        self.assertEqual(LongestPalindromicSubstring.recursive(""), "")
        self.assertEqual(LongestPalindromicSubstring.recursive("a"), "a")
        self.assertEqual(LongestPalindromicSubstring.recursive("aa"), "aa")
        self.assertEqual(LongestPalindromicSubstring.recursive("ac"), "a")
        self.assertEqual(LongestPalindromicSubstring.recursive("babad"), "bab")
        self.assertEqual(LongestPalindromicSubstring.recursive("abcda"), "a")
        LongestPalindromicSubstring.recursive("babaddtattarrattatddetartrateedredividerb")
        # LongestPalindromicSubstring.recursive("euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew")
        # LongestPalindromicSubstring.recursive("vckpzcfezppubykyxvwhbwvgezvannjnnxgaqvesrhdsgngcbbdpqeodzmqbkrwekakrukwxhqjeacxhkixruwshgwkjthmtqumvqcvhhoavarlwhpzbbniqrswvyhtfquioooejsbnxdnjrfhzpdrljcuenzjpzkyrgpxrbtchnzmdkekhmuqpoljvrpndzmogeuxjotdsyrrudligpgwcblaimqdqsgmjrbvyonugzsbkdhawmewiaccuvfnpftcjdjuljekiaipknorknwyx")

if __name__ == '__main__':
    unittest.main()