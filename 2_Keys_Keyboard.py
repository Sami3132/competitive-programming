class Solution:
    def minSteps(self, n: int) -> int:
        myDict = dict()

        def backtrack(count, paste):
            if count == n:
                return 0
            
            if count > n:
                return float("inf")
            
            if (count, paste) in myDict:
                return myDict[(count, paste)]
            
            myDict[(count, paste)] = min(1 + backtrack(count + paste, paste), 2 + backtrack(count * 2, count))
            return myDict[(count, paste)]
        
        if n == 1:
            return 0
        
        return 1 + backtrack(1, 1)
