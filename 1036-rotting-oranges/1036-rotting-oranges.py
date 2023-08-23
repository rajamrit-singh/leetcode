from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        que = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        nonRottedTomatoesFound = False
        encountered = set()
        for r in range(0, ROWS):
            for c in range(0, COLS):
                if(grid[r][c] == 2):
                    que.append((r, c))
                    encountered.add((r, c))
                if (grid[r][c] == 1):
                    nonRottedTomatoesFound = True
        if (len(que) == 0 and nonRottedTomatoesFound):
            return -1
        if (not nonRottedTomatoesFound):
            return 0
        count = 0
        while (len(que) > 0):
            mySet = set()
            for r, c in que:
                if (r - 1 >= 0 and grid[r - 1][c] == 1 and (r - 1, c) not in encountered):
                    mySet.add((r - 1, c))
                    encountered.add((r - 1, c))
                    grid[r - 1][c] = 2
                if (r + 1 < ROWS and grid[r + 1][c] == 1 and (r + 1, c) not in encountered):
                    mySet.add((r + 1, c))
                    encountered.add((r + 1, c))
                    grid[r + 1][c] = 2
                if (c - 1 >= 0 and grid[r][c - 1] == 1  and (r, c - 1) not in encountered):
                    mySet.add((r, c - 1))
                    encountered.add((r - 1, c))
                    grid[r][c - 1] = 2
                if (c + 1 < COLS and grid[r][c + 1] == 1  and (r, c + 1) not in encountered):
                    mySet.add((r, c + 1))
                    encountered.add((r, c + 1))
                    grid[r][c + 1] = 2
            que.clear()
            for pair in mySet:
                que.append(pair)
            if (len(mySet) > 0):
                count += 1
            mySet.clear()
        for r in range(0, ROWS):
            for c in range(0, COLS):
                if(grid[r][c] == 1):
                    return -1
        print(count)
        return count