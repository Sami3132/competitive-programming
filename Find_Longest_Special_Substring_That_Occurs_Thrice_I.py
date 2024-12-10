class Solution:
    def maximumLength(self, s: str) -> int:
        myDict = defaultdict(int)

        i = j = 0
        letter = s[0]
        ans = -1

        while i < len(s):
            if s[i] == letter:
                i += 1
            else:
                words = ""
                
                for k in range(i - j, 0, -1):
                    words += letter
                    myDict[words] += k
                
                j = i
                letter = s[i]
        
        words = ""

        for k in range(i - j, 0, -1):
            words += s[j]
            myDict[words] += k
                
        for key, val in myDict.items():
            if val >= 3:
                ans = max(ans, len(key))
        
        return ans
