class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)

        for el in arr:
            dp[el] = dp[el - difference] + 1
        
        return max(dp.values())
