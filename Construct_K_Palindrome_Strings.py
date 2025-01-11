class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True

        if len(s) < k:
            return False
        
        ans = 0

        for char in set(s):
            if s.count(char) % 2:
                ans += 1
        
        return False if ans > k else True
