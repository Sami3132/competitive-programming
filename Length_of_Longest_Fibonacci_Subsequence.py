class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        mySet = set(arr)
        ans = 0

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr) - 1):
                left, right = arr[i], arr[j]
                curr = left + right
                length = 2

                while curr in mySet:
                    length += 1
                    ans = max(ans, length)
                    left, right = right, curr
                    curr = left + right
        
        return ans
