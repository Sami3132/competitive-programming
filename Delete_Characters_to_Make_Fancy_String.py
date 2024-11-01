class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s
        
        ans = s[: 2]

        for i in range(2, len(s)):
            if not (ans[-1] == s[i] and ans[-2] == s[i]):
                ans += s[i]
        
        return ans
