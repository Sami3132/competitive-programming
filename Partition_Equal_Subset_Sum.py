class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False
        
        mySet = set()
        mySet.add(0)
        target = total // 2

        for i in range(len(nums) - 1, -1, -1):
            newSet = set()
            for el in mySet:
                if el + nums[i] == target:
                    return True

                newSet.add(el + nums[i])
                newSet.add(el)
            
            mySet = newSet
        
        return True if target in mySet else False
