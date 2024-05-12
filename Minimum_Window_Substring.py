class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        map = [0] * 128
        count = len(t)
        start = 0
        end = 0
        minLength = float('inf')
        startIndex = 0

        for char in t:
            map[ord(char)] += 1

        while end < len(s):
            if map[ord(s[end])] > 0:
                count -= 1

            map[ord(s[end])] -= 1
            end += 1

            while count == 0:
                if end - start < minLength:
                    startIndex = start
                    minLength = end - start

                if map[ord(s[start])] == 0:
                    count += 1

                map[ord(s[start])] += 1
                start += 1

        return "" if minLength == float('inf') else s[startIndex:startIndex + minLength]
