class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        maxCount = 0
        i = 1

        while i <= len(arr) - 2:
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                j = i

                while j > 0 and arr[j] > arr[j - 1]:
                    j -= 1
                
                while i < len(arr) - 1 and arr[i] > arr[i + 1]:
                    i += 1
                
                maxCount = max(maxCount, i - j + 1)
            else:
                i += 1
        
        return maxCount
        
