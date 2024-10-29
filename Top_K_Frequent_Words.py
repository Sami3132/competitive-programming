class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        myDict = {}

        for x in words:
            if x in myDict:
                myDict[x] += 1
            else:
                myDict[x] = 1

        res = sorted(myDict, key=lambda x: (-myDict[x], x))

        return res[:k]
