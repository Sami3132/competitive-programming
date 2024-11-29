class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1], grid[1][0]) > 1:
            return -1
        
        heap = [(0, 0, 0)]
        row, col = len(grid), len(grid[0])
        mySet = set()

        while heap:
            t, r, c = heapq.heappop(heap)

            if (r, c) == (row - 1, col - 1):
                return t
            
            neighbor = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

            for nr, nc in neighbor:
                if nr < 0 or nc < 0 or nr == row or nc == col or (nr, nc) in mySet:
                    continue
                
                wait = 0

                if abs(grid[nr][nc] - t) % 2 == 0:
                    wait = 1
                
                time = max(grid[nr][nc] + wait, t + 1)
                heapq.heappush(heap, (time, nr, nc))
                mySet.add((nr, nc))
