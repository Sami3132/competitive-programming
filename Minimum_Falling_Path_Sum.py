class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [([0] * n) for _ in range(n)]
        for i in range(n):
            dp[0][i] = matrix[0][i]
        
        for y in range(1, n):
            for x in range(n):
                temp = dp[y-1][x]
                if x > 0:
                    temp = min(temp, dp[y-1][x-1])
                if x < n - 1:
                    temp = min(temp, dp[y-1][x+1])
                
                dp[y][x] = matrix[y][x] + temp
        
        return min(dp[-1])
