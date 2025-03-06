class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        mySet = set()
        double = missing = None

        for i in range(n):
            for j in range(n):
                if grid[i][j] in mySet:
                    double = grid[i][j]
                
                mySet.add(grid[i][j])
        
        for i in range(1, n ** 2 + 1):
            if i not in mySet:
                missing = i

            if double and missing:
                return [double, missing]
