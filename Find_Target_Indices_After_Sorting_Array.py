class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        newArr = [0 for _ in range(101)]

        for i in range(len(nums)):
            newArr[nums[i]] += 1
        
        for i in range(1, len(newArr)):
            newArr[i] += newArr[i - 1]

        return [x for x in range(newArr[target - 1], newArr[target])]
