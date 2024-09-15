class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}

        ans = 0
        mask = 0
        maskIndex = [-1] * 32

        for i, char in enumerate(s):
            mask = mask ^ vowels.get(char, 0)

            if maskIndex[mask] != -1 or mask == 0:
                length = i - maskIndex[mask]
                ans = max(ans, length)
            else:
                maskIndex[mask] = i
        
        return ans
