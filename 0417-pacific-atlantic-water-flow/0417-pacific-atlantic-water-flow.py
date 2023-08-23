class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set() # Set to keep track of cells that are reachable from pacific ocean
        atl = set() # Set to keep track of cells that are reachable from atlantic ocean
        result = []

        def dfs(row, col, visited, prevHeight):
            if ((row, col) in visited or row < 0 or col < 0 or row == ROWS or col == COLS or heights[row][col] < prevHeight):
                return
            visited.add((row, col))
            # DFS on the neighbouring cells
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            

        # Check which cells can be visited from pacific and atlantic ocean
        for c in range(0, COLS):
            dfs(0, c, pac, prevHeight = 0)
            dfs(ROWS - 1, c, atl, prevHeight = 0)
        
        for r in range(0, ROWS):
            dfs(r, 0, pac, prevHeight = 0)
            dfs(r, COLS - 1, atl, prevHeight = 0)

        # The cells which are common should be added to the result
        for r, c in pac:
            if ((r, c) in atl):
                result.append([r, c])
        return result

