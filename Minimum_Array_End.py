class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = x
        rem = n - 1
        pos = 1

        while rem > 0:
            if not (x & pos):
                ans |= (rem & 1) * pos
                rem >>= 1
            
            pos <<= 1
        
        return ans
