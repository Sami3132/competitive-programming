class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums = Counter(nums)

        for val in nums.values():
            if val % 2:
                return False
        
        return True
