class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n > 0:
            prev = n & 1
            n >>= 1
            curr = n & 1

            if prev == curr:
                return False
        
        return True
