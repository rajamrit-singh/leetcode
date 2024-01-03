class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()
        def dfs(r, c, cur):
            if (cur == len(word)):
                return True
            if (r >= rows or r < 0 or c >= cols or c < 0 or word[cur] != board[r][c] or (r, c) in path):
                return False
            path.add((r, c))
            res = dfs(r - 1, c, cur + 1) or dfs(r + 1, c, cur + 1) or dfs(r, c - 1, cur + 1) or dfs(r, c + 1, cur + 1)
            path.remove((r, c))
            return res
            
        for i in range(rows):
            for j in range(cols):
                if (dfs(i, j, 0)):
                    return True
        return False