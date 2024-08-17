class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        dp = [0] * m
        dp[m - 1] = max(1, 1 - dungeon[n - 1][m - 1])
        
        for i in range(m - 2, -1, -1):
            dp[i] = max(1, dp[i + 1] - dungeon[n - 1][i])
                
        for i in range(n - 2, -1, -1):
            dp[m - 1] = max(1, dp[m - 1] - dungeon[i][m - 1])

            for j in range(m - 2, -1, -1):
                dp[j] = max(1, min(dp[j], dp[j + 1]) - dungeon[i][j])

        return dp[0]
