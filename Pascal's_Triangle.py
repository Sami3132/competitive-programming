class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        ans = [[1], [1, 1]]

        for i in range(1, numRows - 1):
            row = [1]

            for j in range(len(ans[i]) - 1):
                row.append(ans[i][j] + ans[i][j + 1])
            
            row.append(1)
            ans.append(row)
        
        return ans
