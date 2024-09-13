class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        
        ans = []
        
        for left, right in queries:
            total = arr[right]
            remove = arr[left - 1] if left > 0 else 0

            ans.append(total ^ remove)
        
        return ans
