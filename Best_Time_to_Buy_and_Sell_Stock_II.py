class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        j = 0

        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                ans += prices[i] - prices[i - 1]
      
        return ans
