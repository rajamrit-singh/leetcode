class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        up = True
        m = len(mat)
        n = len(mat[0])
        res = []
        row = 0
        col = 0
        while(row < m and col < n):
            if (up):
                while(row > 0 and col < n - 1):
                    res.append(mat[row][col])
                    row -= 1
                    col += 1
                res.append(mat[row][col])
                if (col == n - 1):
                    row += 1
                else:
                    col += 1
            else:
                while(row < m - 1 and col > 0):
                    res.append(mat[row][col])
                    row += 1
                    col -= 1
                res.append(mat[row][col])
                if (row == m - 1):
                    col += 1
                else:
                    row += 1
            up = not up
        return res