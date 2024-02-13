class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = dict()

        for index, num in enumerate(nums):
            complement = target - num

            if complement in store:
                return [store[complement], index]
            store[num] = index
