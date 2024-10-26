class Solution:
    def longestPalindrome(self, s: str) -> int:
        oddCount = 0
        myDict = {}
        
        for ch in s:
            if ch in myDict:
                myDict[ch] += 1
            else:
                myDict[ch] = 1
            if myDict[ch] % 2 == 1:
                oddCount += 1
            else:
                oddCount -= 1
        if oddCount > 1:
            return len(s) - oddCount + 1

        return len(s)
