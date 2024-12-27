class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        maxx = values[0] - 1

        for i in range(1, len(values)):
            ans = max(ans, values[i] + maxx)
            maxx = max(maxx - 1, values[i] - 1)
        
        return ans
