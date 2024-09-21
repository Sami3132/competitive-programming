class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque([(0, 0, 0, 0)])
        visited = set([(0, 0, 0)])
                
        while queue:
            row, col, orientation, moves = queue.popleft()
            
            if orientation == 0 and row == n - 1 and col == n - 2:
                return moves
            
            if orientation == 0:
                if col + 2 < n and grid[row][col + 2] == 0 and (row, col + 1, 0) not in visited:
                    visited.add((row, col + 1, 0))
                    queue.append((row, col + 1, 0, moves + 1))
                    
                if row + 1 < n and grid[row + 1][col] == 0 and grid[row + 1][col + 1] == 0 and (row + 1, col, 0) not in visited:
                    visited.add((row + 1, col, 0))
                    queue.append((row + 1, col, 0, moves + 1))
                    
                if row + 1 < n and grid[row + 1][col] == 0 and grid[row + 1][col + 1] == 0 and (row, col, 1) not in visited:
                    visited.add((row, col, 1))
                    queue.append((row, col, 1, moves + 1))
            
            if orientation == 1:
                if col + 1 < n and grid[row][col + 1] == 0 and grid[row + 1][col + 1] == 0 and (row, col + 1, 1) not in visited:
                    visited.add((row, col + 1, 1))
                    queue.append((row, col + 1, 1, moves + 1))
                
                if row + 2 < n and grid[row+2][col] == 0 and (row + 1, col, 1) not in visited:
                    visited.add((row + 1, col, 1))
                    queue.append((row + 1, col, 1, moves + 1))
                    
                if col + 1 < n and grid[row][col + 1] == 0 and grid[row + 1][col + 1] == 0 and (row, col, 0) not in visited:
                    visited.add((row, col, 0))
                    queue.append((row, col, 0, moves + 1))
        
        return -1
