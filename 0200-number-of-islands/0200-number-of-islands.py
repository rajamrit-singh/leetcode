# Define a function that takes in a 2D grid and returns the number of islands in the grid
class Solution:
    def __init__(self):
        self.n = 0                              # Instance variable to keep track of the number of islands
        self.visited = set()                    # Instance variable to keep track of which nodes have been visited during DFS
        
    def numIslands(self, grid) -> int:
        rows = len(grid)                         # Get the number of rows in the grid
        cols = len(grid[0])                      # Get the number of columns in the grid
        
        # Define a recursive function to perform DFS on a node and determine whether it belongs to an island
        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == '0' or (row, col) in self.visited:
                # Check if the current node is out of bounds, is not part of an island, or has already been visited
                return False
            self.visited.add((row, col))           # Add the current node to the set of visited nodes
            dfs(row-1, col)                        # Check the node to the left
            dfs(row+1, col)                        # Check the node to the right
            dfs(row, col-1)                        # Check the node below
            dfs(row, col+1)                        # Check the node above
            return True
        
        # Iterate over all nodes in the grid and check if they belong to an island
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j):       # Call dfs for the current node and check if an island was found
                    self.n += 1                  # If so, increment the count of islands
        
        # Check if there is a single island represented by a single node that was not visited in the DFS search
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == '1' and (i, j) not in self.visited:
        #             self.n += 1
        
        # Return the total number of islands
        print(self.n)
        return self.n
    
