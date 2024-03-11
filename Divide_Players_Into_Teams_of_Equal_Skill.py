class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2:
            return skill[0] * skill[1]
        
        skill.sort()

        chemistry = 0
        left = 0
        right = len(skill) - 1
        point = skill[left] + skill[right]

        while left < right:
            if skill[left] + skill[right] == point:
                chemistry += skill[left] * skill[right]
            else:
                return -1
            
            left += 1
            right -= 1
        
        return chemistry
