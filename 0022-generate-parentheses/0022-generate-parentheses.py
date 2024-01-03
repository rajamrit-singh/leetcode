class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def generate(cur, opens, close):
            if (len(cur) == n * 2):
                result.append(cur)
                return
            if (opens < n):
                generate(cur + '(', opens + 1, close)
            if (close < opens):
                generate(cur + ')', opens, close + 1)
        generate('', 0, 0)
        return result
        