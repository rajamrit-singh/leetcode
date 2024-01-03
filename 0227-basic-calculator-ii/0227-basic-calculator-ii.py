import re
import math
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = '+'
        # string = str.replace(/\s/g,)
        string = re.sub(r'\s', '', s)
        print(string)
        n = 0
        for index, chr in enumerate(string):
            if (chr.isdigit()):
                n = (n * 10) + int(chr)
            if (not chr.isdigit() or index == len(string) - 1):
                if (sign == '+'):
                    stack.append(n)
                elif (sign == '-'):
                    stack.append(-n)
                elif (sign == '*'):
                    lastInserted = stack.pop()
                    stack.append(lastInserted * n)
                else:
                    lastInserted = stack.pop()
                    ans = lastInserted / n
                    stack.append(math.trunc(ans))
                n = 0
                sign = chr
        print(stack)
        return sum(stack)