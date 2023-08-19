class Solution(object):

    def __init__(self):
        self.maxArea = 0

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        def bfs(row, col, cur, visited):
            # print(row)
            # print(col)
            # print(visited)
            visited.add(str(row) + " " + str(col))
            n1 = 0
            n2 = 0
            n3 = 0
            n4 = 0
            if (row + 1 < rows and grid[row + 1][col] == 1 and ((str(row + 1) + " " + str(col)) not in visited)):
                n1 = bfs(row + 1, col, cur, visited)
            if (row - 1 >= 0 and grid[row - 1][col] == 1 and ((str(row - 1) + " " +  str(col)) not in visited)):
                n2 = bfs(row - 1, col, cur, visited)
            if (col - 1 >= 0 and grid[row][col - 1] == 1 and ((str(row) +  " " + str(col - 1)) not in visited)):
                n3 = bfs(row, col - 1, cur, visited)
            if (col + 1 < cols and grid[row][col + 1] == 1 and ((str(row) + " " +  str(col + 1)) not in visited)):
                n4 = bfs(row, col + 1, cur, visited)
            # print(n1)
            # print(n2)
            # print(n3)
            # print(n4)
            # print('***************')
            return n1 + n2 + n3 + n4 + cur + 1
        
        visited = set()

        for i in range(0, rows):
            for j in range(0, cols):
                if(grid[i][j] == 1):
                    ans = bfs(i, j, 0, visited)
                    if (ans > self.maxArea):
                        self.maxArea = ans
        return self.maxArea


