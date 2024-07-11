class Solution:
    
    def __init__(self):
        self.memo = {}
        
    def uniquePaths(self, m: int, n: int):
        if (m == 1 and n == 1):
            return 1
        if (self.memo.get((m, n))):
            return self.memo.get((m, n))
        if (m > 1 and n > 1):
            self.memo[(m , n)] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        elif (m > 1):
            self.memo[(m, n)] = self.uniquePaths(m - 1, n)
        elif (n > 1):
            self.memo[(m, n)] = self.uniquePaths(m, n - 1)
        return self.memo[(m, n)]