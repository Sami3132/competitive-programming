class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        i = 0

        myDict = defaultdict(int)

        while i < len(s1):
            word = ""

            while i < len(s1) and s1[i] != " ":
                word += s1[i]
                i += 1
            
            print(word)
            myDict[word] += 1
            i += 1
        
        i = 0

        while i < len(s2):
            word = ""

            while i < len(s2) and s2[i] != " ":
                word += s2[i]
                i += 1
            
            myDict[word] += 1
            i += 1
        
        ans = []

        for key, val in myDict.items():
            if val == 1:
                ans.append(key)

        return ans
