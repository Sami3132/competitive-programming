class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        dp = []
        
        for envelope in envelopes:
            height = envelope[1]
            left, right = 0, len(dp) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if dp[mid] < height:
                    left = mid + 1
                else:
                    right = mid - 1
            
            if left == len(dp):
                dp.append(height)
            else:
                dp[left] = height
        
        return len(dp)
