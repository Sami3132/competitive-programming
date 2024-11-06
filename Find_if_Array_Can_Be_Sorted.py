class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        length = len(nums)

        for i in range(length):
            for j in range(i + 1, length):
                if nums[j] < nums[i]:
                    if bin(nums[i]).count('1') != bin(nums[j]).count('1'):
                        return False

                    nums[i], nums[j] = nums[j], nums[i]

        for k in range(length - 1):
            if nums[k] > nums[k + 1]:
                return False

        return True
