class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(i, j):
            mySet = set()
            for x in range(3):
                for y in range(3):
                    val = grid[i + x][j + y]
                    if val < 1 or val > 9 or val in mySet:
                        return False
                    mySet.add(val)
            
            row1 = grid[i][j] + grid[i][j+1] + grid[i][j+2]
            row2 = grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2]
            row3 = grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
            col1 = grid[i][j] + grid[i+1][j] + grid[i+2][j]
            col2 = grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1]
            col3 = grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2]
            diag1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
            diag2 = grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]

            return (row1 == row2 == row3 == col1 == col2 == col3 == diag1 == diag2)

        ans = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if isMagicSquare(i, j):
                    ans += 1
        
        return ans
