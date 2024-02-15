class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 1
        output = list(nums)

        for num in nums:
            if num > 0:
                output[pos] = num
                pos += 2
            else:
                output[neg] = num
                neg += 2
        
        return output
