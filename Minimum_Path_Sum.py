class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        ans = [[float('inf')] * (col + 1) for _ in range(row + 1)]
        ans[row][col - 1] = 0

        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                ans[i][j] = grid[i][j] + min(ans[i + 1][j], ans[i][j + 1])
        
        return ans[0][0]
