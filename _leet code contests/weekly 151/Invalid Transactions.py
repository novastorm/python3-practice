'''
1169. Invalid Transactions

A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.


Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
 

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
'''

from bisect import *
from enum import Enum
from typing import List

class Solution:
    class keys(Enum):
        name = 0
        time = 1
        amount = 2
        city = 3

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        return self.bruteForce(transactions)
    
    def bruteForce(self, transactions: List[str]) -> List[str]:
        class Transaction:
            def __init__(self, string=None, name=None, time=None, amount=None, city=None):
                if string is not None:
                    (name, time, amount, city) = string.split(",")

                self.name = name
                self.time = int(time)
                self.amount = int(amount)
                self.city = city

            def __hash__(self):
                return hash((self.name, self.time, self.amount, self.city))

            def __eq__(self, other):
                if isinstance(other, int):
                    return self.time == other
                if isinstance(other, Transaction):
                    return (
                        self.name == other.name
                        and self.time == other.time
                        and self.amount == other.amount
                        and self.city == other.city
                        )
                raise NotImplemented

            def __ne__(self, other):
                return not self.__eq__(other)

            def __lt__(self, other):
                if isinstance(other, int):
                    return self.time < other
                if isinstance(other, Transaction):
                    if self.name == other.name:
                        return self.time < other.time
                    return self.name < other.name
                raise NotImplemented

            def __gt__(self, other):
                if isinstance(other, int):
                    return self.time > other
                if isinstance(other, Transaction):
                    if self.name == other.name:
                        return self.time > other.time
                    return self.name > other.name
                raise NotImplemented

            def __str__(self):
                return "{},{},{},{}".format(self.name, self.time, self.amount, self.city)

        def find_lt(a, x):
            'Find rightmost value less than x'
            i = bisect_left(a, x)
            if i:
                return a[i-1]
            raise ValueError            
        def find_gt(a, x):
            'Find leftmost value greater than x'
            i = bisect_right(a, x)
            if i != len(a):
                return a[i]
            raise ValueError

        tList = list(map(lambda x: Transaction(x), transactions))
        tList.sort()

        invalidRecords = []

        for i in range(len(tList)):
            # print("-" * 20)
            c = tList[i]
            # print(c)
            if c.amount > 1000:
                invalidRecords.append(c)
                continue

            found = False
            j = i - 1
            while j >= 0:
                p = tList[j]
                if p.name == c.name and p.city != c.city and p.time >= c.time - 60:
                    invalidRecords.append(c)
                    found = True
                    break
                j -= 1

            if found:
                continue

            j = i + 1
            while j < len(tList):
                n = tList[j]
                if n.name == c.name and n.city != c.city and n.time <= c.time + 60:
                    invalidRecords.append(c)
                    break
                j += 1


        results = list(map(lambda r: str(r), invalidRecords))

        return results


###############################################################################

import unittest
# from ReverseASinglyLinkedList import *


class Test_ReverseASinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.S = Solution()

    def test_1(self):
        transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
        expected = ["alice,20,800,mtv","alice,50,100,beijing"]
        self.assertEqual(set(self.S.invalidTransactions(transactions)), set(expected))

    def test_2(self):
        transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
        expected = ["alice,50,1200,mtv"]
        self.assertEqual(set(self.S.invalidTransactions(transactions)), set(expected))

    def test_3(self):
        transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
        expected = ["bob,50,1200,mtv"]
        self.assertEqual(set(self.S.invalidTransactions(transactions)), set(expected))

    def test_4(self):
        transactions = [
            "bob,689,1910,barcelona",
            "alex,696,122,bangkok",
            "bob,832,1726,barcelona",
            "bob,820,596,bangkok",
            "chalicefy,217,669,barcelona",
            "bob,175,221,amsterdam"
            ]
        expected = ["bob,689,1910,barcelona","bob,832,1726,barcelona","bob,820,596,bangkok"]
        self.assertEqual(set(self.S.invalidTransactions(transactions)), set(expected))

    def test_5(self):
        transactions = ["bob,55,173,barcelona","lee,113,952,zurich","maybe,115,1973,madrid","chalicefy,229,283,istanbul","bob,24,874,shanghai","alex,568,412,tokyo","alex,242,1710,milan","iris,722,879,shenzhen","chalicefy,281,1586,warsaw","maybe,246,778,bangkok","xnova,605,166,newdelhi","iris,631,991,hongkong","chalicefy,500,620,tokyo","chalicefy,380,428,istanbul","iris,905,180,barcelona","alex,810,732,shenzhen","iris,689,389,paris","xnova,475,298,singapore","lee,58,709,amsterdam","xnova,717,546,guangzhou","maybe,78,435,shenzhen","maybe,333,145,hongkong","lee,405,1230,hongkong","lee,456,1440,tokyo","chalicefy,286,1071,amsterdam","alex,55,271,shanghai","bob,91,273,warsaw","iris,195,1825,tokyo","maybe,639,417,madrid","maybe,305,882,chicago","lee,443,47,chicago","chalicefy,958,840,budapest","lee,162,1239,budapest","bob,701,505,montreal","alex,52,1575,munich","bob,533,1407,amsterdam","lee,621,491,tokyo","chalicefy,866,622,rome","alex,925,455,hongkong","lee,968,164,moscow","chalicefy,31,1119,newdelhi","iris,527,700,warsaw","bob,286,1694,dubai","maybe,903,29,barcelona","maybe,474,1606,prague","maybe,851,648,beijing","lee,48,655,chicago","maybe,378,25,toronto","lee,922,691,munich","maybe,411,903,taipei","lee,651,112,guangzhou","lee,664,506,dubai","chalicefy,704,924,milan","maybe,333,1264,budapest","chalicefy,587,1112,singapore","maybe,428,437,moscow","lee,721,366,newdelhi","iris,824,1962,beijing","chalicefy,834,489,istanbul","alex,639,1473,zurich","xnova,898,738,tokyo","chalicefy,585,1313,frankfurt","xnova,730,759,beijing","alex,69,892,montreal","lee,77,91,barcelona","lee,722,611,taipei","chalicefy,706,1982,jakarta","chalicefy,743,584,luxembourg","xnova,683,322,istanbul","chalicefy,60,861,prague","alex,366,871,shenzhen","chalicefy,77,870,shenzhen","iris,913,1501,warsaw","iris,846,1176,warsaw","bob,873,69,zurich","alex,601,181,chicago","chalicefy,118,145,hongkong","bob,879,982,montreal","lee,994,950,chicago","maybe,885,1900,shanghai","lee,717,1447,shanghai","chalicefy,71,434,istanbul","bob,870,968,toronto","maybe,718,51,beijing","alex,669,896,istanbul","chalicefy,639,506,rome","alex,594,934,frankfurt","maybe,3,89,jakarta","xnova,328,1710,rome","alex,611,571,chicago","chalicefy,31,458,montreal","iris,973,696,toronto","iris,863,148,rome","chalicefy,926,511,warsaw","alex,218,1411,zurich","chalicefy,544,1296,shenzhen","iris,27,23,montreal","chalicefy,295,263,prague","maybe,575,31,munich","alex,215,174,prague"]
        expected = ["bob,55,173,barcelona","lee,113,952,zurich","maybe,115,1973,madrid","chalicefy,229,283,istanbul","bob,24,874,shanghai","alex,568,412,tokyo","alex,242,1710,milan","iris,722,879,shenzhen","chalicefy,281,1586,warsaw","maybe,246,778,bangkok","iris,631,991,hongkong","chalicefy,500,620,tokyo","iris,905,180,barcelona","iris,689,389,paris","lee,58,709,amsterdam","xnova,717,546,guangzhou","maybe,78,435,shenzhen","maybe,333,145,hongkong","lee,405,1230,hongkong","lee,456,1440,tokyo","chalicefy,286,1071,amsterdam","alex,55,271,shanghai","bob,91,273,warsaw","iris,195,1825,tokyo","maybe,305,882,chicago","lee,443,47,chicago","chalicefy,958,840,budapest","lee,162,1239,budapest","alex,52,1575,munich","bob,533,1407,amsterdam","lee,621,491,tokyo","chalicefy,866,622,rome","lee,968,164,moscow","chalicefy,31,1119,newdelhi","bob,286,1694,dubai","maybe,903,29,barcelona","maybe,474,1606,prague","maybe,851,648,beijing","lee,48,655,chicago","maybe,378,25,toronto","lee,922,691,munich","maybe,411,903,taipei","lee,651,112,guangzhou","lee,664,506,dubai","chalicefy,704,924,milan","maybe,333,1264,budapest","chalicefy,587,1112,singapore","maybe,428,437,moscow","lee,721,366,newdelhi","iris,824,1962,beijing","chalicefy,834,489,istanbul","alex,639,1473,zurich","chalicefy,585,1313,frankfurt","xnova,730,759,beijing","alex,69,892,montreal","lee,77,91,barcelona","lee,722,611,taipei","chalicefy,706,1982,jakarta","chalicefy,743,584,luxembourg","xnova,683,322,istanbul","chalicefy,60,861,prague","chalicefy,77,870,shenzhen","iris,913,1501,warsaw","iris,846,1176,warsaw","bob,873,69,zurich","alex,601,181,chicago","chalicefy,118,145,hongkong","bob,879,982,montreal","lee,994,950,chicago","maybe,885,1900,shanghai","lee,717,1447,shanghai","chalicefy,71,434,istanbul","bob,870,968,toronto","alex,669,896,istanbul","chalicefy,639,506,rome","alex,594,934,frankfurt","xnova,328,1710,rome","alex,611,571,chicago","chalicefy,31,458,montreal","iris,973,696,toronto","iris,863,148,rome","chalicefy,926,511,warsaw","alex,218,1411,zurich","chalicefy,544,1296,shenzhen","chalicefy,295,263,prague","alex,215,174,prague"]
        self.assertEqual(set(self.S.invalidTransactions(transactions)), set(expected))

    def test_6(self):
        transactions = ["bob,649,842,prague","alex,175,1127,mexico","iris,164,119,paris","lee,991,1570,mexico","lee,895,1876,taipei","iris,716,754,moscow","chalicefy,19,592,singapore","chalicefy,820,71,newdelhi","maybe,231,1790,paris","lee,158,987,mexico","chalicefy,415,22,montreal","iris,803,691,milan","xnova,786,804,guangzhou","lee,734,1915,prague","bob,836,1904,dubai","iris,666,231,chicago","iris,677,1451,milan","maybe,860,517,toronto","iris,344,1452,bangkok","lee,664,463,frankfurt","chalicefy,95,1222,montreal","lee,293,1102,istanbul","maybe,874,36,hongkong","maybe,457,1802,montreal","xnova,535,270,munich","iris,39,264,istanbul","chalicefy,548,363,barcelona","lee,373,184,munich","xnova,405,957,mexico","chalicefy,517,266,luxembourg","iris,25,657,singapore","bob,688,451,beijing","bob,263,1258,tokyo","maybe,140,222,amsterdam","xnova,852,330,barcelona","xnova,589,837,budapest","lee,152,981,mexico","alex,893,1976,shenzhen","xnova,560,825,prague","chalicefy,283,399,zurich","iris,967,1119,guangzhou","alex,924,223,milan","chalicefy,212,1865,chicago","alex,443,537,taipei","maybe,390,5,shanghai","bob,510,1923,madrid","bob,798,343,hongkong","iris,643,1703,madrid","bob,478,928,barcelona","maybe,75,1980,shanghai","xnova,293,24,newdelhi","iris,176,268,milan","alex,783,81,moscow","maybe,560,587,milan","alex,406,776,istanbul","lee,558,727,paris","maybe,481,1504,munich","maybe,685,602,madrid","iris,678,788,madrid","xnova,704,274,newdelhi","chalicefy,36,1984,paris","iris,749,200,amsterdam","lee,21,119,taipei","iris,406,433,bangkok","bob,777,542,taipei","maybe,230,1434,barcelona","iris,420,1818,zurich","lee,622,194,amsterdam","maybe,545,608,shanghai","xnova,201,1375,madrid","lee,432,520,dubai","bob,150,1634,singapore","maybe,467,1178,munich","iris,45,904,beijing","maybe,607,1953,tokyo","bob,901,815,tokyo","maybe,636,558,milan","bob,568,1674,toronto","iris,825,484,madrid","iris,951,930,dubai","bob,465,1080,taipei","bob,337,593,chicago","chalicefy,16,176,rome","chalicefy,671,583,singapore","iris,268,391,chicago","xnova,836,153,jakarta","bob,436,530,warsaw","alex,354,1328,luxembourg","iris,928,1565,paris","xnova,627,834,budapest","xnova,640,513,jakarta","alex,119,16,toronto","xnova,443,1687,taipei","chalicefy,867,1520,montreal","alex,456,889,newdelhi","lee,166,3,madrid","bob,65,1559,zurich","alex,628,861,moscow","maybe,668,572,mexico","bob,402,922,montreal"]
        expected = ["bob,649,842,prague","alex,175,1127,mexico","iris,164,119,paris","lee,991,1570,mexico","lee,895,1876,taipei","iris,716,754,moscow","chalicefy,19,592,singapore","chalicefy,820,71,newdelhi","maybe,231,1790,paris","lee,158,987,mexico","iris,803,691,milan","xnova,786,804,guangzhou","lee,734,1915,prague","bob,836,1904,dubai","iris,666,231,chicago","iris,677,1451,milan","maybe,860,517,toronto","iris,344,1452,bangkok","lee,664,463,frankfurt","chalicefy,95,1222,montreal","lee,293,1102,istanbul","maybe,874,36,hongkong","maybe,457,1802,montreal","xnova,535,270,munich","iris,39,264,istanbul","chalicefy,548,363,barcelona","lee,373,184,munich","xnova,405,957,mexico","chalicefy,517,266,luxembourg","iris,25,657,singapore","bob,688,451,beijing","bob,263,1258,tokyo","xnova,852,330,barcelona","xnova,589,837,budapest","lee,152,981,mexico","alex,893,1976,shenzhen","xnova,560,825,prague","iris,967,1119,guangzhou","alex,924,223,milan","chalicefy,212,1865,chicago","alex,443,537,taipei","bob,510,1923,madrid","bob,798,343,hongkong","iris,643,1703,madrid","bob,478,928,barcelona","maybe,75,1980,shanghai","iris,176,268,milan","maybe,560,587,milan","alex,406,776,istanbul","maybe,481,1504,munich","maybe,685,602,madrid","iris,678,788,madrid","chalicefy,36,1984,paris","iris,749,200,amsterdam","iris,406,433,bangkok","bob,777,542,taipei","maybe,230,1434,barcelona","iris,420,1818,zurich","lee,622,194,amsterdam","maybe,545,608,shanghai","xnova,201,1375,madrid","lee,432,520,dubai","bob,150,1634,singapore","maybe,467,1178,munich","iris,45,904,beijing","maybe,607,1953,tokyo","maybe,636,558,milan","bob,568,1674,toronto","iris,825,484,madrid","iris,951,930,dubai","bob,465,1080,taipei","chalicefy,16,176,rome","xnova,836,153,jakarta","bob,436,530,warsaw","alex,354,1328,luxembourg","iris,928,1565,paris","xnova,627,834,budapest","xnova,640,513,jakarta","alex,119,16,toronto","xnova,443,1687,taipei","chalicefy,867,1520,montreal","alex,456,889,newdelhi","lee,166,3,madrid","bob,65,1559,zurich","maybe,668,572,mexico","bob,402,922,montreal"]
        self.assertEqual(set(self.S.invalidTransactions(transactions)), set(expected))


if __name__ == '__main__':
        unittest.main()
