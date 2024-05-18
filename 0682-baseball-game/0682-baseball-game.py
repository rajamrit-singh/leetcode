class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if (self.isDigit(i)):
                stack.append(int(i))
            elif (i == "C"):
                stack.pop()
            elif (i == "D"):
                stack.append(stack[-1] * 2)
            else:
                stack.append(stack[-1] + stack[-2])
        return sum(stack)
    
    def isDigit(self, n):
        try:
            if (int(n)):
                return True
        except:
            return False