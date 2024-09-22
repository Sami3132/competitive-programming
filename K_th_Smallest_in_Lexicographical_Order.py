class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        i = 1

        def count(curr):
            neighbor = curr + 1
            res = 0

            while curr <= n:
                res += min(neighbor, n + 1) - curr
                curr *= 10
                neighbor *= 10
            
            return res

        while i < k:
            steps = count(curr)

            if i + steps <= k:
                curr += 1
                i += steps
            else:
                curr *= 10
                i += 1
        
        return curr
