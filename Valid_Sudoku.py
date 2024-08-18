class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square = set()

        for i in range(9):
            row = set()
            col = set()

            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in row:
                        row.add(board[i][j])
                    else:
                        return False
                if board[j][i] != ".":
                    if board[j][i] not in col:
                        col.add(board[j][i])
                    else:
                        return False
            
                if board[i][j] != '.':
                    subArr = (i // 3) * 3 + (j // 3)
                    sqrStr = f"{subArr}-{board[i][j]}"
                    
                    if sqrStr not in square:
                        square.add(sqrStr)
                    else:
                        return False

        return True
