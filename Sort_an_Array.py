class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(nums):
            if len(nums) == 1:
                return nums
            
            mid = len(nums) // 2
            
            leftHalf = mergeSort(nums[:mid])
            rightHalf = mergeSort(nums[mid:])

            return merge(leftHalf, rightHalf)
        
        def merge(leftHalf, rightHalf):
            mergedArr = []

            i = j = 0

            while i < len(leftHalf) and j < len(rightHalf):
                if leftHalf[i] < rightHalf[j]:
                    mergedArr.append(leftHalf[i])
                    i += 1
                else:
                    mergedArr.append(rightHalf[j])
                    j += 1
            
            while i < len(leftHalf):
                mergedArr.append(leftHalf[i])
                i += 1
            
            while j < len(rightHalf):
                mergedArr.append(rightHalf[j])
                j += 1
            
            return mergedArr
        
        return mergeSort(nums)
