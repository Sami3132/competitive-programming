class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
                return 0
            
            total = grid[i][j]
            grid[i][j] = 0

            total += dfs(i + 1, j)
            total += dfs(i, j + 1)
            total += dfs(i - 1, j)
            total += dfs(i, j - 1)
            
            return total
                    
        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    ans = max(ans, dfs(i, j))

        return ans
