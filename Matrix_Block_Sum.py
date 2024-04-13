class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
            
        col, row = len(mat), len( mat[0])
        newArr = [ [ 0 for i in range(row) ] for x in range(col) ]
        
        for i in range(0, col):
            total = 0
            
            for j in range(0, row):
                total += mat[i][j]
                newArr[i][j] = total
                
                if i > 0:
                    newArr[i][j] += newArr[i - 1][j]
        
        output_image = [ [ 0 for i in range(row) ] for j in range(col) ]
        
        for i in range(col):
            for j in range(row):                
                minRow, maxRow = max( 0, i - K), min( col - 1, i + K)
                minCol, maxCol = max( 0, j - K), min( row - 1, j + K)
                
                output_image[i][j] = newArr[maxRow][maxCol]
                
                if minRow > 0:
                    output_image[i][j] -= newArr[minRow - 1][maxCol]
                
                if minCol > 0:
                    output_image[i][j] -= newArr[maxRow][minCol - 1]
                    
                if minCol > 0 and minRow > 0:
                    output_image[i][j] += newArr[minRow-1][minCol - 1]
                
        return output_image
