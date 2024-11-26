class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0] * n

        for l, r in edges:
            incoming[r] += 1
        
        nonIncoming = []

        for i, el in enumerate(incoming):
            if not el:
                nonIncoming.append(i)
            
            if len(nonIncoming) > 1:
                return -1
        
        return nonIncoming[0]
