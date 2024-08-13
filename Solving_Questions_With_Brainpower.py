class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = dict()

        for i in range(len(questions) - 1, -1, -1):
            dp[i] = max(dp.get(i + 1, 0), questions[i][0] + dp.get(1 + i + questions[i][1], 0))
        
        return dp[0]
