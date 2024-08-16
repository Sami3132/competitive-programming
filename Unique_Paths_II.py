class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * m
        dp[m - 1] = 1

        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                elif j + 1 < m:
                    dp[j] = dp[j + 1] + dp[j]
                                
        return dp[0]
