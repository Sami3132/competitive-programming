class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s):
            return s
            
        myDict = defaultdict(str)
        i = 0

        ans = ""

        while i < len(s):
            j = 0

            while i < len(s) and j < numRows:
                myDict[j] += s[i]
                i += 1
                j += 1
            
            j -= 2

            while i < len(s) and j > 0:
                myDict[j] += s[i]
                i += 1
                j -= 1
    
        for key, value in myDict.items():
            ans += value
        
        return ans
