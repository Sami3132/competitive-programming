class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        myDict = defaultdict(int)
        
        def maxScore(nums: List, left: int, right: int):
            if left == right:
                return nums[left]
            
            if (left, right) in myDict:
                return myDict[(left, right)]

            leftSum = nums[left] - maxScore(nums, left + 1, right)
            rightSum = nums[right] - maxScore(nums, left, right - 1)
            
            myDict[(left, right)] = max(leftSum, rightSum)
            return myDict[(left, right)]

        return maxScore(nums, left = 0, right = len(nums) - 1) >= 0
