class Solution:

    def evaluateInorderExpression(inputStr):

        class InvalidExpression(Exception):
            pass

        precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '(': 0,
            ')': 0
        }

        def isOperand(c):
            try:
                int(c)
            except ValueError:
                return False

            return True

        def isOperator(c):
            return c in '+-*/()'

        def parseInput(inputStr):
            return inputStr.split()

        def convertToPostorderFromInorder(inputList):
            result = []
            stack = []

            for c in inputList:
                if not isOperand(c) and not isOperator(c):
                    raise InvalidExpression

                if isOperand(c):
                    result.append(c)
                    continue

                if c == '(':
                    stack.append(c)
                    continue

                if c ==')':
                    while stack and stack[-1] != '(':
                        e = stack.pop()
                        result.append(e)
                    if stack and stack[-1] != '(':
                        raise InvalidExpression
                    stack.pop()
                    continue

                if not isOperator(c):
                    raise InvalidExpression

                while stack and precedence[stack[-1]] > precedence[c]:
                    e = stack.pop()
                    result.append(e)

                stack.append(c)

            while stack:
                result.append(stack.pop())

            return result

        def evaluatePostorder(inputList):
            result = []
            for c in inputList:
                if isOperand(c):
                    result.append(int(c))
                    continue

                y = result.pop()

                if c == '-':
                    if not result:
                        result.append(-y)
                    else:
                        x = result.pop()
                        result.append(x - y)
                    continue

                if not result:
                    raise InvalidExpression
                x = result.pop()

                if c == '+':
                    result.append(x + y)
                    continue

                if c == '*':
                    result.append(x * y)
                    continue

                if c == '/':
                    if y == 0:
                        raise ZeroDivisionError
                    result.append(x / y)
                    continue

                raise InvalidExpression

            if len(result) > 1:
                raise InvalidExpression

            return result[0]

        inputExpression = parseInput(inputStr)
        postorderExpression = convertToPostorderFromInorder(inputExpression)
        return evaluatePostorder(postorderExpression)


###############################################################################

import unittest


class Test_EvaluateInorderExpression(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        inputStr = '- ( 3 + ( 2 - 1 ) )'
        expected = '-4'
        self.assertTrue(Solution.evaluateInorderExpression(inputStr),expected)

    def test_2(self):
        inputStr = '- 2 - 3'
        expected = '-5'
        self.assertTrue(Solution.evaluateInorderExpression(inputStr),expected)

    def test_3(self):
        inputStr = '- ( - 2 - 3 )'
        expected = '5'
        self.assertTrue(Solution.evaluateInorderExpression(inputStr),expected)

    def test_4(self):
        inputStr = '- ( -2 + -3 )'
        expected = '5'
        self.assertTrue(Solution.evaluateInorderExpression(inputStr),expected)

if __name__ == '__main__':
        unittest.main()
