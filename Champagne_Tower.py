class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [poured]

        for row in range(1, query_row + 1):
            newDP = [0] * (row + 1)

            for i in range(row):
                if dp[i] >= 1:
                    newDP[i] += (dp[i] - 1) / 2
                    newDP[i + 1] += (dp[i] - 1) / 2
            
            dp = newDP

        return min(1, dp[query_glass])
