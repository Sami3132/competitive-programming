class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""

        while columnNumber > 0:
            ans = chr(ord('A') + (columnNumber - 1) % 26) + ans
            columnNumber = (columnNumber - 1) // 26
        
        return ans
