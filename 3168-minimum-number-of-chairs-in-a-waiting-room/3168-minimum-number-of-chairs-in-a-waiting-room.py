class Solution:
    def minimumChairs(self, s: str) -> int:
        minChair = 1
        current = 1
        for char in s[1::]:
            print(char)
            print(current)
            if char == 'E':
                current += 1
            else:
                current -= 1
            if (current > minChair):
                minChair = current
                
        return minChair