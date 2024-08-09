class Solution:
    def tribonacci(self, n: int) -> int:
        newArr = [-1 for i in range(n + 1)]

        def dp(n):
            if n < 2:
                return n
            if n == 2:
                return 1
            
            if newArr[n] == -1:
                newArr[n] = dp(n - 1) + dp(n - 2) + dp(n - 3)
            
            return newArr[n]
        
        return dp(n)
