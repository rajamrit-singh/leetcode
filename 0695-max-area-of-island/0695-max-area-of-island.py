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
        #Before looking at this bfs code, go through the code below this method
        def bfs(row, col, visited):
            # Adding the current row and col to the visited set
            # Space between row and col to differentiate b/w Row - 1 and col 17("1 17") and row 11 col 7 ("11 7")
            visited.add(str(row) + " " + str(col))
            n1 = 0
            n2 = 0
            n3 = 0
            n4 = 0
            if (row + 1 < rows and grid[row + 1][col] == 1 and ((str(row + 1) + " " + str(col)) not in visited)):
                n1 = bfs(row + 1, col,  visited)
            if (row - 1 >= 0 and grid[row - 1][col] == 1 and ((str(row - 1) + " " +  str(col)) not in visited)):
                n2 = bfs(row - 1, col,  visited)
            if (col - 1 >= 0 and grid[row][col - 1] == 1 and ((str(row) +  " " + str(col - 1)) not in visited)):
                n3 = bfs(row, col - 1,  visited)
            if (col + 1 < cols and grid[row][col + 1] == 1 and ((str(row) + " " +  str(col + 1)) not in visited)):
                n4 = bfs(row, col + 1,  visited)

            return n1 + n2 + n3 + n4  + 1
        
        visited = set() #Create a set to keep track of all the visited elements

        for i in range(0, rows):
            for j in range(0, cols):
                # If the value of a grid space is 1, then we need to run dfs on that
                if(grid[i][j] == 1):
                    ans = bfs(i, j, visited)
                    if (ans > self.maxArea):
                        self.maxArea = ans
        return self.maxArea


