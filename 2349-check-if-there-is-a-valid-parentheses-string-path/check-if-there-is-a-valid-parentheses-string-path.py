class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        if (m + n- 1) % 2 == 1:
            return False
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i, j ,bal):
            if bal < 0:
                return False
            if grid[i][j] == '(':
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False
            if i == m - 1 and j == n - 1:
                return bal == 0
            if i + 1 < m and dfs(i + 1, j , bal):
                return True
            if j + 1 < n and dfs(i , j + 1, bal):
                return True
            return False
        return dfs(0, 0, 0)
        