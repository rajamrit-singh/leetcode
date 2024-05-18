class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if (char != '*'):
                stack.append(char)
            else:
                stack.pop()
        result = ""
        for i in stack:
            result += i
        return result