class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def dfs():
            total = 0

            for tiles in count:
                if count[tiles] > 0:
                    count[tiles] -= 1
                    total += 1 + dfs()
                    count[tiles] += 1
                
            return total
        
        return dfs()
