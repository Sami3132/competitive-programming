class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        sumNoDel = sumDel = ans = arr[0]
        
        for num in arr[1:]:
            sumDel = max(sumDel + num, num, sumNoDel)
            sumNoDel = max(sumNoDel + num, num)
            ans = max(ans, sumNoDel, sumDel)

        return ans
