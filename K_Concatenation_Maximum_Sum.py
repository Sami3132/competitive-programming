class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        total = sum(arr)
        maxSum = self.maxSubArraySum(arr)
        
        if k == 1:
            return maxSum % MOD
        
        jointmaxSum = self.maxSubArraySum(arr * 2)
        if total > 0:
            return (jointmaxSum + (k - 2) * total) % MOD
        
        return jointmaxSum % MOD
        
    def maxSubArraySum(self, arr: List[int]) -> int:
        maxSum = float("-inf")
        total = 0
        
        for el in arr:
            total += el
            
            if total < 0:
                total = 0
            
            maxSum = max(maxSum, total)
        
        return maxSum
