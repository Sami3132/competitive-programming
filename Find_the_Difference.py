class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict1 = dict()

        for i in s:
            dict1[i] = dict1.get(i, 0) + 1

        for i in t:
            if i not in dict1 or dict1[i] == 0:
                return i
            dict1[i] -= 1
        
        return ""
