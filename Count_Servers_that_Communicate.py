class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        ans = 0        
        points = []
        compRow = [0] * rows
        compCol = [0] * cols
        
        for rowI in range(rows):
            for colI in range(cols):
                if grid[rowI][colI]:
                    points.append((rowI, colI))
                    compRow[rowI] += 1
                    compCol[colI] += 1 
        
        for rowI, colI in points:
            if compRow[rowI] > 1 or compCol[colI] > 1 :
                ans += 1                      
        
        return ans
