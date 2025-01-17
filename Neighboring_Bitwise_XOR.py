class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        first = last = 0

        for el in derived:
            if el:
                last = ~last
        
        return first == last
