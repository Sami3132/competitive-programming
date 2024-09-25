from collections import defaultdict

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        myDict = defaultdict(int)

        for word in words:
            newWord = ""
            for char in word:
                newWord += char
                myDict[newWord] += 1
        
        ans = []
        for word in words:
            newWord = ""
            score = 0
            for char in word:
                newWord += char
                score += myDict[newWord]
            ans.append(score)
        
        return ans
