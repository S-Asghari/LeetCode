import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[-1])

        def isNum(n):
            if n == '+' or n == '-' or n == '*' or n == '/':
                return False
            else:
                return True 
        
        def operate(operator, x, y):
            if operator == '+':
                return int(x) + int(y)
            elif operator == '-':
                return int(x) - int(y)
            elif operator == '*':
                return int(x) * int(y)
            else:
                return math.trunc(int(x) / int(y))
        
        tokens.reverse()
        s = []

        while tokens:
            while isNum(tokens[-1]):
                s.append(tokens.pop())
            operator = tokens.pop()
            num2 = s.pop()
            num1 = s.pop()
            tmp_result = operate(operator, num1, num2)
            s.append(tmp_result)

        return s[-1]