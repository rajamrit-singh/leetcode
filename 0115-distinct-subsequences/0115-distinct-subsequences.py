class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        self.memo = {}
        def dfs(current, index):
            length = len(current)
            # if (current != t[:length]):
            #     return 0
            if((current, index) in self.memo):
                return self.memo.get((current, index))
            if (current == t):
                return 1
            if (len(current) == len(t) or index >= len(s)):
                return 0
            if (s[index] == t[length]):                
                res1 = dfs(current + s[index], index + 1)
            else:
                res1 = 0
            res2 = dfs(current, index + 1)
            self.memo[(current, index)] = res1 + res2
            return res1 + res2
        
        result = dfs("", 0)
        return result