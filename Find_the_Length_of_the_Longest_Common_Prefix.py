class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) > len(arr2):
            arr2, arr1 = arr1, arr2
        
        mySet = set()

        for el in arr1:
            while el and el not in mySet:
                mySet.add(el)
                el //= 10
        
        ans = 0

        for el in arr2:
            while el and el not in mySet:
                el //= 10
            
            if el:
                ans = max(ans, len(str(el)))
        
        return ans
