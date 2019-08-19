class LongestPalindromicSubstring:
    @staticmethod
    def bruteforce_v1(s):
        """Test all combinations"""
        if not s:
            return s

        result = ""

        for i in range(len(s)):
            j = i + 1
            while j <= len(s):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(result):
                    result = s[i:j]
                j += 1

        return result

    @staticmethod
    def bruteforce_v2(s):
        """
        Test all combinations with length greater than best last result
        """
        if not s:
            return s

        result = ""

        for i in range(len(s)):
            j = i + 1
            while j <= len(s) and len(result) <= len(s[i:]):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(result):
                    result = s[i:j]
                j += 1

        return result

    @staticmethod
    def bruteforce_v3(s):
        """
        Test all combinations 
        with length greater than best last result
        with optimized string slicing
        """
        if not s:
            return s

        result = ""

        for i in range(len(s)):
            j = i + 1
            while j <= len(s) and len(result) <= len(s[i:]):
                testStr = s[i:j]
                if testStr == testStr[::-1] and len(testStr) > len(result):
                    result = testStr
                j += 1

        return result

    @staticmethod
    def bruteforce(s):
        return LongestPalindromicSubstring.bruteforce_v3(s)

    @staticmethod
    def recursive_v1(s):
        # print(s)
        if len(s) <= 1:
            return s

        if len(s) == 2 and s[0] == s[1]:
            return s

        if s[0] == s[-1]:
            result = LongestPalindromicSubstring.recursive_v1(s[1:-1])
            if len(result) == len(s) - 2:
                return s[0] + result + s[-1]

        strA = LongestPalindromicSubstring.recursive_v1(s[:-1])
        strB = LongestPalindromicSubstring.recursive_v1(s[1:])
        return strA if len(strA) >= len(strB) else strB

    @staticmethod
    def recursive_v2(s):
        def helper(s, i, j):
            # print(i, j, s[i:j+1])
            if i == j:
                return s[i:j+1]

            if i + 1 == j and s[i] == s[j]:
                return s[i:j+1]

            if s[i] == s[j]:
                result = helper(s, i+1, j-1)
                if len(result) == j - i + 1 - 2:
                    return s[i] + result + s[j]

            strA = helper(s, i, j-1)
            strB = helper(s, i+1, j)
            return strA if len(strA) >= len(strB) else strB

        return helper(s, 0, len(s)-1)

    @staticmethod
    def recursive_v3(s):
        def helper(s, i, j):
            # print(i, j, s[i:j+1])
            if i == j:
                return (i,j)

            if i + 1 == j and s[i] == s[j]:
                return (i,j)

            if s[i] == s[j]:
                result = helper(s, i+1, j-1)
                if result == (i+1,j-1):
                    return (i,j)

            strA = helper(s, i, j-1)
            strB = helper(s, i+1, j)
            return strA if (strA[1]-strA[0]+1) >= strB[1]-strB[0]+1 else strB

        result = helper(s, 0, len(s)-1)
        return s[result[0]:result[1]+1]

    @staticmethod
    def recursive_v4(s):
        if len(s) == 0:
            return s

        memo = {}
        def helper(s, i, j):
            if ((i,j) in memo):
                print("cache hit", (i,j), memo[(i,j)], s[i:j+1])
                return memo[(i,j)]
            print(i, j, s[i:j+1])

            if i == j:
                m = (j-i+1,i,j)
                memo[(i,j)] = m
                return m

            if i + 1 == j and s[i] == s[j]:
                m = (j-i+1,i,j)
                memo[(i,j)] = m
                return (2,i,j)

            if s[i] == s[j]:
                result = helper(s, i+1, j-1)
                memo[(i+1, j-1)] = result
                if result[0] == j-i+1 - 2:
                    m = (j-i+1,i,j)
                    memo[(i,j)] = m
                    return m

            strA = helper(s, i, j-1)
            memo[(i,j-1)] = strA
            strB = helper(s, i+1, j)
            memo[(i+1,j)] = strB
            return strA if strA[0] >= strB[0] else strB

        result = helper(s, 0, len(s)-1)
        print("result", result, s[result[1]:result[2]+1])
        return s[result[1]:result[2]+1]

    @staticmethod
    def recursive(s):
        return LongestPalindromicSubstring.recursive_v4(s)
