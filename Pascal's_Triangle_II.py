class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1] * (rowIndex + 1)
        if rowIndex == 0: return ans
        
        newArr = self.getRow(rowIndex - 1)

        for i in range(1, len(ans) - 1):
            ans[i] = newArr[i - 1] + newArr[i]
        
        return ans
