class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            val = mid * (mid + 1) // 2

            if val <= n:
                left = mid + 1
            else:
                right = mid - 1
        
        return right