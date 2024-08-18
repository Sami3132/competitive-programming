class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter = len(arr) // 4
        i, j = 0, 0
        
        while i < len(arr):
            while j < len(arr) and arr[i] == arr[j]:
                j += 1
            
            if j - i > quarter:
                return arr[i]
            
            i = j
