class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(row, col, k):
            notInRow = k not in board[row]
            notInCol = k not in [board[i][col] for i in range(9)]
            notInSqr = k not in [board[i][j] for i in range(row // 3 * 3, row // 3 * 3 + 3) for j in range(col // 3 * 3, col // 3 * 3 + 3)]

            return notInRow and notInCol and notInSqr
        
        def solve(row, col):
            if row == 9:
                return True
            if col == 9:
                return solve(row + 1, 0)
            if board[row][col] != '.':
                return solve(row, col + 1)
            else:
                for k in range(1, 10):
                    if isValid(row, col, str(k)):
                        board[row][col] = str(k)
                        if solve(row, col + 1):
                            return True
                        board[row][col] = '.'
                
                return False
        
        solve(0, 0)
