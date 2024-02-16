class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        pacMan = sum([abs(0 - target[0]), abs(0 - target[1])])

        for x, y in ghosts:
            if pacMan >= sum([abs(x - target[0]), abs(y - target[1])]):
                return False
        
        return True
