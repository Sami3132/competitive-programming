class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        myDict = dict()

        def dp(i, j):
            if len(s) - i < len(t) - j:
                return 0
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            
            if (i, j) in myDict:
                return myDict[(i, j)]
            
            if s[i] == t[j]:
                myDict[(i, j)] = dp(i + 1, j + 1) + dp(i + 1, j)
            else:
                myDict[(i, j)] = dp(i + 1, j)
            
            return myDict[(i, j)]
        
        return dp(0, 0)
