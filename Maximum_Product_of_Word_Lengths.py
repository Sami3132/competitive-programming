class Solution:
    def maxProduct(self, words: List[str]) -> int:
        myDict = defaultdict(int)

        for word in words:
            bitwise = 0

            for char in word:
                bitwise |= (1 << ord(char) - 97)
            
            myDict[word] = bitwise
        
        ans = 0
        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not(myDict[words[i]] & myDict[words[j]]):
                    ans = max(ans, len(words[i]) * len(words[j]))
        
        return ans
