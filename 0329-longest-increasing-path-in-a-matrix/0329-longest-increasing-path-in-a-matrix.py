class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        # [up, down]
        rows = len(matrix)
        cols = len(matrix[0])
        dp_lip = [[0] * cols for i in range(rows)]
        
        def dfs(lip, row, col):
            up, down, left, right = 0, 0, 0, 0
            if (lip[row][col] != 0):
                return lip[row][col]
            if (row - 1 >= 0 and matrix[row - 1][col] > matrix[row][col]):
                up = dfs(lip, row - 1, col)
            if (row + 1 < rows and matrix[row + 1][col] > matrix[row][col]):
                down = dfs(lip, row + 1, col)
            if (col - 1 >= 0 and matrix[row][col - 1] > matrix[row][col]):
                left = dfs(lip, row, col - 1)
            if (col + 1 < cols and matrix[row][col + 1] > matrix[row][col]):
                right = dfs(lip, row, col + 1)
            lip[row][col] = 1 + max(up, down, left, right)
            return 1 + max(up, down, left, right)
             
        maxValue = 1
        for i in range(0, rows):
            for j in range(0, cols):
                dfs(dp_lip, i, j)
        for i in range(0, rows):
            for j in range(0, cols):
                maxValue = max(maxValue, dp_lip[i][j])
        return maxValue