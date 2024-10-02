class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        myDict = {el: i + 1 for i, el in enumerate(sorted(set(arr)))}
        
        return list(map(myDict.get, arr))
