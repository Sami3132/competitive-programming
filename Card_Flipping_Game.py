class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = {x for i, x in enumerate(fronts) if x == backs[i]}
        res = 9999

        for i in range(len(fronts)):
            if fronts[i] not in same: res = min(res, fronts[i])
            if backs[i] not in same: res = min(res, backs[i])
            
        return res % 9999
